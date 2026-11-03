import csv
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_project import validate, sha256


class ValidateProjectTests(unittest.TestCase):
    def make_project(self, root: Path) -> Path:
        required_dirs = ["research", "data/raw", "data/processed", "scripts", "results/tables",
                         "results/figures", "results/validation", "logs", "report"]
        for rel in required_dirs:
            (root / rel).mkdir(parents=True, exist_ok=True)
        required_files = ["README.md", "research/problem_statement.md", "research/research_questions.md",
                          "research/analysis_protocol.md", "data/data_dictionary.csv", "logs/execution_status.md"]
        for rel in required_files:
            (root / rel).write_text("test content\n", encoding="utf-8")
        dataset = root / "data/raw/sample.csv"
        dataset.write_text("x\n1\n", encoding="utf-8")
        with (root / "data/dataset_register.csv").open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["dataset_id", "title", "producer", "landing_page", "licence",
                                                   "accessed_utc", "local_path", "sha256", "redistribution_status"])
            writer.writeheader()
            writer.writerow({"dataset_id": "sample", "title": "Sample", "producer": "Test source",
                             "landing_page": "https://example.org", "licence": "CC0",
                             "accessed_utc": "2026-01-01T00:00:00Z", "local_path": "data/raw/sample.csv",
                             "sha256": sha256(dataset), "redistribution_status": "OPEN_LICENSE"})
        (root / "report/final_report.md").write_text("# Report\n", encoding="utf-8")
        return root

    def test_valid_project_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = self.make_project(Path(tmp) / "project")
            result = validate(project)
            self.assertEqual(result["status"], "PASS", result["errors"])
            self.assertTrue(any(x.startswith("sha256:") for x in result["checked"]))

    def test_hash_mismatch_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = self.make_project(Path(tmp) / "project")
            (project / "data/raw/sample.csv").write_text("x\n999\n", encoding="utf-8")
            result = validate(project)
            self.assertEqual(result["status"], "FAIL")
            self.assertTrue(any("SHA-256 mismatch" in e for e in result["errors"]))

    def test_missing_report_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = self.make_project(Path(tmp) / "project")
            (project / "report/final_report.md").unlink()
            result = validate(project)
            self.assertEqual(result["status"], "FAIL")
            self.assertTrue(any("exactly one canonical report" in e for e in result["errors"]))

    def test_two_reports_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = self.make_project(Path(tmp) / "project")
            (project / "report/second_report.pdf").write_bytes(b"not a real pdf but nonempty")
            result = validate(project)
            self.assertEqual(result["status"], "FAIL")

    def test_path_traversal_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = self.make_project(Path(tmp) / "project")
            p = project / "data/dataset_register.csv"
            text = p.read_text(encoding="utf-8").replace("data/raw/sample.csv", "../../secret.csv")
            p.write_text(text, encoding="utf-8")
            result = validate(project)
            self.assertEqual(result["status"], "FAIL")
            self.assertTrue(any("Unsafe local_path" in e for e in result["errors"]))


if __name__ == "__main__":
    unittest.main()
