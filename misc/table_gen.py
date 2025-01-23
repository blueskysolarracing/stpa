from stpa.examples.stpa_handbook import UNSAFE_CONTROL_ACTIONS
from abc import ABC, abstractmethod
from typing import ClassVar
from stpa import UnsafeControlAction
import pandas as pd
from textwrap import wrap
from pylatex.utils import escape_latex

class LatexTableGenerator(ABC):
    
    COLUMN_NAMES : ClassVar[list[str]] = []
    _COLUMN_WIDTHS_CM = {}
    
    @staticmethod
    def _escape_latex(text: str) -> str:
        """Escape LaTeX special characters in the given text."""
        
        escape_extensions = {
            '>': r'\textgreater{}',
            '<': r'\textless{}',
        }
        
        escaped = escape_latex(text)
        
        for orig, repl in escape_extensions.items():
            escaped = escaped.replace(orig, repl)
            
        return escaped
    
    def generate(self):
        """Generate a LaTeX table with proper formatting. Assumes that the table is being generated in a document with the following packages:
        - array
        - graphicx
        """
        
        df = self.get_all_row_values()
        df = df[self.COLUMN_NAMES]
        
        latex = [
            
            '\\newcolumntype{R}[1]{>{\\raggedright\\arraybackslash}p{#1}}',
            '\\begin{table}[h]',
            '\\resizebox{\\textwidth}{!}{%\n'
            '\\begin{tabular}{|' + '|'.join([f'R{{{self._COLUMN_WIDTHS_CM[column]:.2f}cm}}' for column in self.COLUMN_NAMES]) + '|}',
            '\\hline'
        ]
        
        headers = [f'\\textbf{{{self._escape_latex(col)}}}' for col in self.COLUMN_NAMES]
        latex.append(' & '.join(headers) + ' \\\\')
        latex.append('\\hline')
        
        for _, row in df.iterrows():
            formatted_row = [self._escape_latex(cell) for cell in row]
            latex.append(' & '.join(formatted_row) + ' \\\\ ')
            latex.append('\\hline')
        
        latex.extend([
            '\\end{tabular}',
            '}',
            '\\end{table}'
        ])
        
        return '\n'.join(latex)
    

    @abstractmethod
    def get_all_row_values(self) -> pd.DataFrame:
        """
        Returns a list of all row values for the table being generated.
        """ 
        pass
    
class UCATableGenerator(LatexTableGenerator, ABC):
    
    def __init__(self, unsafe_control_actions: list[UnsafeControlAction]):
        """Initialize the UCATableGenerator with a list of unsafe control actions.

        Args:
            unsafe_control_actions (list[UnsafeControlAction]): A list of unsafe control actions to be included in the table.
        """
        
        self.unsafe_control_actions = unsafe_control_actions
    
class UCAAttributeTableGenerator(UCATableGenerator):
    
    COLUMN_NAMES : ClassVar[list[str]] = ["Source", "Name", "Type", "Control Action", "Context", "Hazards"]
    _COLUMN_WIDTHS_CM : ClassVar[dict[str, float]] = {
        "Source": 2,
        "Name": 2,
        "Type": 2,
        "Control Action": 3,
        "Context": 3,
        "Hazards": 4
    }
    
    def get_all_row_values(self) -> pd.DataFrame:
        """
        Returns a list of all row values for the table being generated.
        """
        
        rows = []
        for uca in self.unsafe_control_actions:
            row = [
                uca.source,
                uca.name,
                uca.type_.replace(' {} ', ' '),
                uca.control_action,
                uca.context,
                "\n\n".join([str(h) for h in uca.hazards])
            ]
            rows.append(row)
            

        df = pd.DataFrame(rows, columns=self.COLUMN_NAMES)
        return df
    
if __name__ == "__main__":
    
    uca_table_generator = UCAAttributeTableGenerator(UNSAFE_CONTROL_ACTIONS[0:5])
    latex = uca_table_generator.generate()
    with open("misc/resources/uca_table.tex", "w") as f:
        f.write(latex)
    
    
        
        
        
        
        