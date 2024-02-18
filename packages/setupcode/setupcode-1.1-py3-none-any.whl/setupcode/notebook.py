def autoreload():
    from IPython import get_ipython

    """Import this function in a jupyter notebook and run it to enable autoreload of modules"""
    get_ipython().run_line_magic("load_ext", "autoreload")
    get_ipython().run_line_magic("autoreload", "2")


def output_transparent():
    from IPython import get_ipython

    """Import this function in a jupyter notebook and run it to set the background to transparent"""
    get_ipython().run_cell_magic(
        "html",
        "",  # NOTE not a specific cell
        """
        <style>
        .cell-output-ipywidget-background {background-color: transparent !important;}
        .jp-OutputArea-output {background-color: transparent;}
        </style>
        """,
    )


class _PlotlyRender:
    def default(self):
        """Do not change the default plotly renderer of fig.show()"""
        self._set_renderer(None)

    def minimal_filesize(self):
        """Figures are not saved inside the notebook, works only with fig.show()"""
        self._set_renderer("mokeypatch")

    def github_svg(self):
        """Plots are displayed on GitHub and in HTML exports without creating large files."""
        self._set_renderer("svg")

    def github_png(self):
        self._set_renderer("png")

    def notebook(self):
        self._set_renderer("notebook")

    def vscode(self):
        self._set_renderer("vscode")

    def custom(self, renderer: str):
        """
        "browser": opens plots in a browser window
        For more options see: https://plotly.com/python/renderers/
        """
        self._set_renderer(renderer)

    def _set_renderer(self, renderer: str):
        import plotly.io as pio
        from IPython.display import display
        from plotly.basedatatypes import BaseFigure

        if renderer == "mokeypatch":

            def show(self, *args, **kwargs):
                """This function monkey patches (modifies at runtime) behavior of fig.show()."""
                display(
                    self,
                    # raw=True,
                )

        else:
            pio.renderers.default = renderer

            def show(self, *args, **kwargs):
                "Default implementation of fig.show()"
                return pio.show(self, *args, **kwargs)

        BaseFigure.show = show


plotly_render = _PlotlyRender()


class _PlotlyThemeVbt:
    def github_dark(self):
        import plotly.graph_objects as go
        import plotly.io as pio
        import vectorbtpro as vbt

        pio.templates["my_theme"] = go.layout.Template(
            layout_paper_bgcolor="#22272E",
            layout_plot_bgcolor="#22272E",
        )
        vbt.settings["plotting"]["layout"]["template"] = "vbt_dark+my_theme"

    def solarized_dark(self):
        import plotly.graph_objects as go
        import plotly.io as pio
        import vectorbtpro as vbt

        pio.templates["my_theme"] = go.layout.Template(
            layout_paper_bgcolor="#00212B",
            layout_plot_bgcolor="#00212B",
        )
        vbt.settings["plotting"]["layout"]["template"] = "vbt_dark+my_theme"

    def solarized_light(self):
        import plotly.graph_objects as go
        import plotly.io as pio
        import vectorbtpro as vbt

        pio.templates["my_theme"] = go.layout.Template(
            layout_paper_bgcolor="#F7F0E0",
        )
        vbt.settings["plotting"]["layout"]["template"] = "vbt_light+my_theme"


plotly_theme_vbt = _PlotlyThemeVbt()
