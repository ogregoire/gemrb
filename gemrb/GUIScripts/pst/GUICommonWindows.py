# -*-python-*-
# GemRB - Infinity Engine Emulator
# Copyright (C) 2003 The GemRB Project
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
# $Header: /data/gemrb/cvs2svn/gemrb/gemrb/gemrb/GUIScripts/pst/GUICommonWindows.py,v 1.8 2004/04/26 12:59:20 edheldil Exp $


# GUICommonWindows.py - functions to open common windows in lower part of the screen

import GemRB
from GUIDefines import *

TimeWindow = None
PortWindow = None
MenuWindow = None
MainWindow = None

# Buttons:
# 0 CNTREACH
# 1 INVNT
# 2 MAP
# 3 MAGE
# 4 AI
# 5 STATS
# 6 JRNL
# 7 PRIEST
# 8 OPTION
# 9 REST
# 10 TXTE

def OpenCommonWindows ():
	global TimeWindow, PortWindow, MenuWindow, MainWindow

	TimeWindow = GemRB.LoadWindow (0)
	PortWindow = GemRB.LoadWindow (1)
	MenuWindow = GemRB.LoadWindow (2)
	MainWindow = GemRB.LoadWindow (3)

	Window = MenuWindow

	# Can't Reach ???
	Button = GemRB.GetControl (Window, 0)
	GemRB.SetButtonState (Window, Button, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "CntReachPress")

	# AI
	Button = GemRB.GetControl (Window, 4)
	GemRB.SetButtonState (Window, Button, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "AIPress")

	# Message popup
	Button = GemRB.GetControl (Window, 10)
	GemRB.SetButtonState (Window, Button, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "TxtePress")


	SetupMenuWindowControls (Window)


	GemRB.SetVisible (TimeWindow, 1)
	GemRB.SetVisible (PortWindow, 1)
	GemRB.SetVisible (MenuWindow, 1)
	GemRB.SetVisible (MainWindow, 1)
	
def CloseCommonWindows ():
	global MainWindow

	if MainWindow == None:
		return
	#if TimeWindow == None:
	#	return
	
	GemRB.UnloadWindow (MainWindow)
	GemRB.UnloadWindow (TimeWindow)
	GemRB.UnloadWindow (PortWindow)
	GemRB.UnloadWindow (MenuWindow)

	MainWindow = None

def SetupMenuWindowControls (Window):
	# Inventory
	Button = GemRB.GetControl (Window, 1)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenInventoryWindow")

	# Map
	Button = GemRB.GetControl (Window, 2)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenMapWindow")

	# Mage
	Button = GemRB.GetControl (Window, 3)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenMageWindow")
	# Stats
	Button = GemRB.GetControl (Window, 5)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenRecordsWindow")

	# Journal
	Button = GemRB.GetControl (Window, 6)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenJournalWindow")

	# Priest
	Button = GemRB.GetControl (Window, 7)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenPriestWindow")

	# Options
	Button = GemRB.GetControl (Window, 8)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenOptionsWindow")

	# Rest
	Button = GemRB.GetControl (Window, 9)
	GemRB.SetEvent(Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenStoreWindow")


	# AI
	Button = GemRB.GetControl (Window, 4)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenFloatMenuWindow")

	# Can't Reach ???
	Button = GemRB.GetControl (Window, 0)
	#GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenFormationWindow")
	#GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenPartyManageWindow")
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenContainerWindow")


def CntReachPress ():
	print "CntReachPress"

def AIPress ():
	print "AIPress"

def TxtePress ():
	print "TxtePress"

def RestPress ():
	print "RestPress"


# which=0: inventory; 1: rec screen
def GetActorPortrait (actor, which):
	#return GemRB.GetPlayerPortrait( actor, which)

	name = GemRB.GetPlayerName (actor, 0)
	if name == 'Nameless One':
		#p = 'NOA'
		#p = 'NOC'
		#p = 'NOD'
		#p = 'NOF'
		#p = 'NOH'
		#p = 'NOM'
		#p = 'NOS'
		p = 'NOZ'
	elif name == 'Annah':
		p = 'ANN'
	elif name == "Dak'kon":
		p = 'DKK'
	elif name == 'Fall-from-Grace':
		p = 'FFG'
	elif name == 'Morte':
		p = 'MRT'
	elif name == 'Nodrom':
		p = 'NDM'
	elif name == 'Ignus':
		p = 'IGY'
	elif name == 'Vhailor':
		p = 'VHA'
	else:
		print 'Unknown name:', name
		return None

	if which == 0:
		return 'IVP' + p
	else:
		return 'STP' + p


SelectionChangeHandler = None

def SetSelectionChangeHandler (handler):
	global SelectionChangeHandler
	SelectionChangeHandler = handler

def RunSelectionChangeHandler ():
	if SelectionChangeHandler:
		SelectionChangeHandler ()
