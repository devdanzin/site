from pysite.base_route import RedirectView


class GitHubView(RedirectView):
    path = "/github"
    name = "github"
    page = "https://gitlab.com/discord-python/"
    code = 302
