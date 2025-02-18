from stpa.examples.stpa_handbook import UNSAFE_CONTROL_ACTIONS, app_c_aas_defs, app_c_abscua_defs, app_c_ahtvo_defs, app_c_wbscafc_defs, c2_defs
from abc import ABC, abstractmethod
from typing import ClassVar
from stpa import UnsafeControlAction
import pandas as pd
from textwrap import wrap
from pylatex.utils import escape_latex
import re
from collections import defaultdict
from enum import Enum

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
            # '\\begin{table}[h]',
            # '\\resizebox{\\textwidth}{!}{%\n'
            '\\begin{tabularx}{\\textwidth}{|' + '|'.join([f'R{{{self._COLUMN_WIDTHS_CM.get(column, 2):.2f}cm}}' for column in self.COLUMN_NAMES]) + '|}',
            '\\hline'
        ]
        
        headers = [f'\\textbf{{{self._escape_latex(col)}}}' for col in self.COLUMN_NAMES]
        latex.append(' & '.join(headers) + ' \\\\')
        latex.append('\\hline')
        
        for _, row in df.iterrows():
            formatted_row = [self._escape_latex(cell) if cell else 'N/A' for cell in row]
            latex.append(' & '.join(formatted_row) + ' \\\\ ')
            latex.append('\\hline')
        
        latex.extend([
            '\\end{tabularx}',
            # '}',
            # '\\end{table}'
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
    
class UCAAttributesTableGenerator(UCATableGenerator):
    
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
    
    

class UCAType:
    NEGATIVE = "NEGATIVE"
    POSITIVE = "POSITIVE"
    TIMING = "TIMING"
    STATE_CHANGE = "STATE_CHANGE"
    UNKNOWN = "UNKNOWN"
    
class UCAByTypesTableGenerator(UCATableGenerator):
    
    COLUMN_NAMES : ClassVar[list[str]] = ["Control Action", 
                                          "Providing causes hazard", 
                                          "Not providing causes hazard",
                                          "Incorrect timing/order",
                                          "Stopped too soon/Applied too long"]
    _COLUMN_WIDTHS_CM : ClassVar[dict[str, float]] = {
        "Control Action": 2,
        "Providing causes hazard": 3,
        "Not providing causes hazard": 3,
        "Incorrect timing/order": 3,
        "Stopped too soon/Applied too long": 3,
    }
    
    @staticmethod
    def categorize_uca_type(uca_type: str) -> UCAType:
        """
        Categorizes a control action string into main types:
        - NEGATIVE: Does not provide/perform
        - POSITIVE: Provides/performs (without timing)
        - TIMING: Provides too early/late/long/before/after
        - STATE_CHANGE: Stops/continues providing
        - UNKNOWN: Doesn't match known patterns
        """
        
        # Normalize string to lowercase for matching
        type = uca_type.lower()
        
        # Negative patterns
        if re.match(r"does not (provide|perform|arm|power|disarm)", type):
            return UCAType.NEGATIVE
        
        # State change patterns
        if re.match(r"(stops|continues)", type):
            return UCAType.STATE_CHANGE
        
        # Timing patterns
        timing_words = r"(before|after|early|late|long|until|more than)"
        if re.search(fr"provides.*{timing_words}", type) or \
        re.search(fr"performs.*{timing_words}", type):
            return UCAType.TIMING
        
        # Basic positive patterns (without timing)
        if re.match(r"(provides|performs|arms|powers|disarms|armed)", type):
            return UCAType.POSITIVE
            
        return UCAType.UNKNOWN

    def get_all_row_values(self) -> pd.DataFrame:
        """
        Returns a list of all row values for the table being generated.
        """
        
        control_actions_to_ucas= defaultdict(list[UnsafeControlAction])
        
        for uca in self.unsafe_control_actions:
            
            for key in control_actions_to_ucas.keys():
                if uca.control_action in key or key in uca.control_action:
                    control_actions_to_ucas[key].append(uca)
                    break
            else:
                control_actions_to_ucas[uca.control_action].append(uca)
            
        rows = []
            
        for control_action, ucas in control_actions_to_ucas.items():
            new_row = [control_action]
            ucas_by_type = {
                UCAType.NEGATIVE: [],
                UCAType.POSITIVE: [],
                UCAType.TIMING: [],
                UCAType.STATE_CHANGE: []
            }
            for uca in ucas:
                uca_type = self.categorize_uca_type(uca.type_)
                ucas_by_type[uca_type].append(uca)
            
            new_row.append("\n\n".join([str(uca) for uca in ucas_by_type[UCAType.POSITIVE]]))
            new_row.append("\n\n".join([str(uca) for uca in ucas_by_type[UCAType.NEGATIVE]]))
            new_row.append("\n\n".join([str(uca) for uca in ucas_by_type[UCAType.TIMING]]))
            new_row.append("\n\n".join([str(uca) for uca in ucas_by_type[UCAType.STATE_CHANGE]]))
            
            rows.append(new_row)
            
        df = pd.DataFrame(rows, columns=self.COLUMN_NAMES)
        return df
        
        
        
        
        
        
if __name__ == "__main__":
    
    uca_table_generator = UCAAttributesTableGenerator(UNSAFE_CONTROL_ACTIONS)
    latex = uca_table_generator.generate()
    with open("misc/resources/all_ucas.tex", "w") as f:
        f.write(latex)
    
    
        
        
        
        
        