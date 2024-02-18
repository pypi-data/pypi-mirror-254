import subprocess
from rpy2.robjects import r


def check_pkg_installed():
    """Check if a package is installed in R."""
    return len(r("system.file(package = 'learningmachine')")) > 0


# paste0("c(", paste0("'", rownames(installed.packages()), "'", collapse = ","), ")")
# c('cli','cpp11','digest','dplyr','ellipsis','evaluate','fansi','fastmap','generics','glue','highr','htmltools','jsonlite','knitr','lifecycle','magrittr','pillar','pkgconfig','purrr','R6','Rcpp','remotes','repr','rlang','skimr','stringi','stringr','tibble','tidyr','tidyselect','utf8','vctrs','withr','xfun','yaml','base','boot','class','cluster','codetools','compiler','datasets','foreign','graphics','grDevices','grid','KernSmooth','lattice','MASS','Matrix','methods','mgcv','nlme','nnet','parallel','rpart','spatial','splines','stats','stats4','survival','tcltk','tools','utils')


def check_install_r_pkg():
    """Install an R package."""
    if check_pkg_installed() == False:
        try:
            r(
                "utils::install.packages(c('cli','cpp11','digest','dplyr','ellipsis','evaluate','fansi','fastmap','generics','glue','highr','htmltools','jsonlite','knitr','lifecycle','magrittr','pillar','pkgconfig','purrr','R6','Rcpp','remotes','repr','rlang','skimr','stringi','stringr','tibble','tidyr','tidyselect','utf8','vctrs','withr','xfun','yaml','base','boot','class','cluster','codetools','compiler','datasets','foreign','graphics','grDevices','grid','KernSmooth','lattice','MASS','Matrix','methods','mgcv','nlme','nnet','parallel','rpart','spatial','splines','stats','stats4','survival','tcltk','tools','utils'), repos = 'https://cran.r-project.org', dependencies = TRUE)"
            )
            r"options(repos = c(techtonique = 'https://techtonique.r-universe.dev', CRAN = 'https://cloud.r-project.org')); install.packages('learningmachine', dependencies = TRUE)"
        except Exception as e1:
            try:
                r(
                    "utils::install.packages(c('cli','cpp11','digest','dplyr','ellipsis','evaluate','fansi','fastmap','generics','glue','highr','htmltools','jsonlite','knitr','lifecycle','magrittr','pillar','pkgconfig','purrr','R6','Rcpp','remotes','repr','rlang','skimr','stringi','stringr','tibble','tidyr','tidyselect','utf8','vctrs','withr','xfun','yaml','base','boot','class','cluster','codetools','compiler','datasets','foreign','graphics','grDevices','grid','KernSmooth','lattice','MASS','Matrix','methods','mgcv','nlme','nnet','parallel','rpart','spatial','splines','stats','stats4','survival','tcltk','tools','utils'), repos = c('https://techtonique.r-universe.dev', 'https://cran.r-project.org'), lib = '.', dependencies = TRUE)"
                )
                r"options(repos = c(techtonique = 'https://techtonique.r-universe.dev', CRAN = 'https://cloud.r-project.org')); install.packages('learningmachine', dependencies = TRUE, lib='.')"

            except Exception as e2:
                try:
                    subprocess.run(
                        [
                            "Rscript",
                            "-e",
                            "utils::install.packages(c('cli','cpp11','digest','dplyr','ellipsis','evaluate','fansi','fastmap','generics','glue','highr','htmltools','jsonlite','knitr','lifecycle','magrittr','pillar','pkgconfig','purrr','R6','Rcpp','remotes','repr','rlang','skimr','stringi','stringr','tibble','tidyr','tidyselect','utf8','vctrs','withr','xfun','yaml','base','boot','class','cluster','codetools','compiler','datasets','foreign','graphics','grDevices','grid','KernSmooth','lattice','MASS','Matrix','methods','mgcv','nlme','nnet','parallel','rpart','spatial','splines','stats','stats4','survival','tcltk','tools','utils'), repos = 'https://techtonique.r-universe.dev', dependencies = TRUE)",
                        ]
                    )
                    subprocess.run(
                        [
                            "Rscript",
                            "-e",
                            "options(repos = c(techtonique = 'https://techtonique.r-universe.dev', CRAN = 'https://cloud.r-project.org')); install.packages('learningmachine', dependencies = TRUE)",
                        ]
                    )
                except Exception as e3:
                    subprocess.run(
                        [
                            "Rscript",
                            "-e",
                            "utils::install.packages(c('cli','cpp11','digest','dplyr','ellipsis','evaluate','fansi','fastmap','generics','glue','highr','htmltools','jsonlite','knitr','learningmachine','lifecycle','magrittr','pillar','pkgconfig','purrr','R6','Rcpp','remotes','repr','rlang','skimr','stringi','stringr','tibble','tidyr','tidyselect','utf8','vctrs','withr','xfun','yaml','base','boot','class','cluster','codetools','compiler','datasets','foreign','graphics','grDevices','grid','KernSmooth','lattice','MASS','Matrix','methods','mgcv','nlme','nnet','parallel','rpart','spatial','splines','stats','stats4','survival','tcltk','tools','utils'), repos = 'https://cran.r-project.org', lib = '.', dependencies = TRUE)",
                        ]
                    )
                    subprocess.run(
                        [
                            "Rscript",
                            "-e",
                            "options(repos = c(techtonique = 'https://techtonique.r-universe.dev', CRAN = 'https://cloud.r-project.org')); install.packages('learningmachine', lib='.', dependencies = TRUE)",
                        ]
                    )
    if check_pkg_installed() == True:
        return 1
    return 0
