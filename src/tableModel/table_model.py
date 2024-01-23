from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtGui import QColor, QBrush, QIcon
import pandas as pd

class ConstrucaoModeloTabela(QAbstractTableModel):
    
    def __init__(self, dados: pd.DataFrame):
        QAbstractTableModel.__init__(self)
        self.df_dados: pd.DataFrame = dados


    def rowCount(self, parent=QModelIndex) -> int:
        return len(self.df_dados.index)

    def columnCount(self, parent=QModelIndex) -> int:
        return len(self.df_dados.columns)       

    def data(self, index: QModelIndex, role: int):
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole:
                return str(self.df_dados.iloc[index.row(), index.column()])
    
    def headerData(self, section: int, orientation, role: int):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self.df_dados.columns[section])
            elif orientation == Qt.Orientation.Vertical:
                return str(self.df_dados.index[section])
        return None