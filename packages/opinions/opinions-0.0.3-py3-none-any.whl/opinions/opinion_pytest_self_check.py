from . import Opinion


class PytestSelfCheckOpionion(Opinion):
    def apply_changes(self):
        if self.project.pyproject.content.get("tool", {}).get("poetry", {}).get("name", None) != "opinions":
            self.project.pyproject.add_pytest_opt("--opinions")
