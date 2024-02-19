import subprocess
from functools import lru_cache
from rpy2.robjects import r
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import StrVector
from sklearn.base import BaseEstimator

base = importr("base")
stats = importr("stats")


@lru_cache(maxsize=32)
def load_learningmachine():
    # Install R packages
    commands1_lm = 'base::system.file(package = "learningmachine")'  # check "learningmachine" is installed
    commands2_lm = 'base::system.file("learningmachine_r", package = "learningmachine")'  # check "learningmachine" is installed locally
    exec_commands1_lm = subprocess.run(
        ["Rscript", "-e", commands1_lm], capture_output=True, text=True
    )
    exec_commands2_lm = subprocess.run(
        ["Rscript", "-e", commands2_lm], capture_output=True, text=True
    )
    if (
        len(exec_commands1_lm.stdout) == 7
        and len(exec_commands2_lm.stdout) == 7
    ):  # kind of convoluted, but works
        print("Installing R packages along with 'learningmachine'...")
        commands1 = [
            'try(utils::install.packages(c("R6", "Rcpp", "skimr"), repos="https://cloud.r-project.org", dependencies = TRUE), silent=TRUE)',
            'try(utils::install.packages("learningmachine", repos="https://techtonique.r-universe.dev", dependencies = TRUE), silent=TRUE)',
        ]
        commands2 = [
            'try(utils::install.packages(c("R6", "Rcpp", "skimr"), lib="./learningmachine_r", repos="https://cloud.r-project.org", dependencies = TRUE), silent=TRUE)',
            'try(utils::install.packages("learningmachine", lib="./learningmachine_r", repos="https://techtonique.r-universe.dev", dependencies = TRUE), silent=TRUE)',
        ]
        try:
            for cmd in commands1:
                subprocess.run(["Rscript", "-e", cmd])
        except Exception as e:  # can't install packages globally
            subprocess.run(["mkdir", "learningmachine_r"])
            for cmd in commands2:
                subprocess.run(["Rscript", "-e", cmd])

        try:
            base.library(StrVector(["learningmachine"]))
        except (
            Exception
        ) as e1:  # can't load the package from the global environment
            try:
                base.library(
                    StrVector(["learningmachine"]), lib_loc="learningmachine_r"
                )
            except Exception as e2:  # well, we tried
                try:
                    r("try(library('learningmachine'), silence=TRUE)")
                except (
                    NotImplementedError
                ) as e3:  # well, we tried everything at this point
                    r(
                        "try(library('learningmachine', lib.loc='learningmachine_r'), silence=TRUE)"
                    )


class Base(BaseEstimator):
    """
    Base class.
    """

    def __init__(self):
        """
        Initialize the model.
        """
        self.type_fit = None
        self.obj = None
        load_learningmachine()
