""" Strucutre Registration

"""


try:
    from rekuest.structures.default import get_default_structure_registry, Scope
    from rekuest.widgets import SearchWidget

    from konviktion.api.schema import (
        GithubRepoFragment,
        aget_github_repo,
        SearchGithubRepoQuery,
    )

    structure_reg = get_default_structure_registry()
    structure_reg.register_as_structure(
        GithubRepoFragment,
        identifier="@port/githubrepo",
        scope=Scope.GLOBAL,
        expand=aget_github_repo,
        default_widget=SearchWidget(query=SearchGithubRepoQuery.Meta.document, ward="konviktion"),
    )

except ImportError:
    structure_reg = None
