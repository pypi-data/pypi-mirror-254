"""
******************************************************************************

    Echoes Data Browser (Ebrow) is a data navigation and report generation
    tool for Echoes.
    Echoes is a RF spectrograph for SDR devices designed for meteor scatter
    Both copyright (C) 2018-2023
    Giuseppe Massimo Bertani gm_bertani(a)yahoo.it

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, http://www.gnu.org/copyleft/gpl.html

*******************************************************************************

"""

from PyQt5.QtWidgets import QColorDialog, QWidget, QButtonGroup, QFileDialog
from PyQt5.QtGui import QColor, QIcon, QPixmap
from datetime import datetime
from edb.logprint import print
from edb.dateintervaldialog import DateIntervalDialog
from edb.utilities import splitASCIIdumpFile, splitBinaryDumpFile, mkExportFolder


class HasHead(QWidget):
    """
    This filter detects the presence of a head echo.
    It cannot rely on Raise front data uniquely, they
    must be integrated with information taken
    from the related dump file, so this filter
    cannot work if dumps are disabled and evalFilter()
    will return always False in this case
    """
    def __init__(self, parent, ui, settings):
        self._ui = ui
        self._parent = parent
        self._settings = settings

    def evalFilter(self, evId: int) -> bool:
        """
        calculates if the given event satisfies this filter
        """
        df = self._parent.datasource.getEventData(evId)

        datName, datData, dailyNr, utcDate = self._parent.dataSource.extractDumpData(evId)
        if datName is not None and datData is not None:
            if ".datb" in datName:
                dfMap, dfPower = splitBinaryDumpFile(datData)
            else:
                dfMap, dfPower = splitASCIIdumpFile(datData)

    def getParameters(self):
        """
        displays the parametrization dialog
        and gets the user's settings
        """
        pass

    def load(self):
        """
        loads this filter's parameters
        from settings file
        """
        pass

    def save(self):
        """
        save ths filter's parameters
        to settings file
        """
        pass
