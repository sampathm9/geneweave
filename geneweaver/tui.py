from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, ProgressBar

class GeneWeaverApp(App):
    TITLE = "GeneWeaver"
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("GPU-Accelerated CRISPR Alignment Engine")
        yield Static("Genome processing")
        yield ProgressBar(total=100, show_eta=True)
        yield Static("FASTA -> Alignment -> Scoring -> Ranking")
        yield Footer()

if __name__ == "__main__":
    GeneWeaverApp().run()
