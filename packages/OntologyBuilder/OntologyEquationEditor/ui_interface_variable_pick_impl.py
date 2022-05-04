#!/usr/local/bin/python3
# encoding: utf-8
"""
@summary:      An editor for designing ontologies in my context
@contact:      heinz.preisig@chemeng.ntnu.no
@requires:     Python 3 or higher
@since:        2022-04-03
@version:      0.1
@change:       2022-04-03
@author:       Preisig, Heinz A
@copyright:    2022 Preisig, Heinz A  All rights reserved.
"""

__author__ = 'Preisig, Heinz A'

MAX_HEIGHT = 800

from PyQt5 import QtCore

from Common.resources_icons import roundButton
from OntologyBuilder.OntologyEquationEditor.variable_table import VariableTable


class UI_VariableTableInterfacePick(VariableTable):
  """
  dialog for a variable
  emits a signal on completion
  """
  #
  # completed = QtCore.pyqtSignal(str)
  picked = QtCore.pyqtSignal(int)
  # new_variable = QtCore.pyqtSignal(str)
  # new_equation = QtCore.pyqtSignal(str, str)
  # deleted_symbol = QtCore.pyqtSignal(str)

  def __init__(self,
               title,
               variables,
               indices,
               network,
               enabled_types=['ALL'],
               hide_vars=[],
               hide_columns=[],
               info_file=None,
               hidden=[]
               ):
    """
    constructs a dialog window based on QDialog for picking variables
    @param title:     title string: indicates the tree's nature
    @param variables: physical variable.
    @network:      network type
    @my_types:      type of variables being processed

    control is done through the interface and additional functions:
    - enable_pick_contents : true or false
    - enable_seclection : rows and columns

    signals:
    - picked : returns selected item text
    - completed : button finished has been pressed
    -
    """

    VariableTable.__init__(self,
                           title,
                           "variable_picking",
                           variables,
                           indices,
                           network,
                           # variables.index_accessible_variables_on_networks,
                           enabled_types,
                           hide_vars,
                           hide_columns,
                           info_file=info_file
                           )
    buttons = {}
    buttons["back"] = self.ui.pushFinished
    buttons["info"] = self.ui.pushInfo
    buttons["new"] = self.ui.pushNew
    buttons["port"] = self.ui.pushPort
    buttons["dot"] = self.ui.pushDot
    buttons["tex"] = self.ui.pushLaTex

    hidden = ["new", "port", "info", "dot", "tex"]

    roundButton(buttons["back"], "back", tooltip="go back")
    # roundButton(buttons["info"], "info", tooltip="information")

    # roundButton(buttons["new"], "new", tooltip="new variable")
    # roundButton(buttons["port"], "port", tooltip="new port variable")
    for b in hidden:
      buttons[b].hide()
    self.variable_list = []
    self.hide_columns = hide_columns

    self.setToolTips('pick')
    self.ui.tableVariable.setToolTip("click on row to copy variable to expression")
    self.ui.tableVariable.setSortingEnabled(True)

  def on_tableVariable_itemClicked(self, item):
    row = int(item.row())
    item = self.ui.tableVariable.item
    var_ID = int(item(row,9).text()) #str(item(row, 1).text())
    self.picked.emit(var_ID)
    return

  def on_tableVariable_itemDoubleClicked(self, item):
    print("debugging -- double click on item", item.row(), item.column())

  def on_pushFinished_pressed(self):
    self.close()

  def closeEvent(self, event):
    self.close()
