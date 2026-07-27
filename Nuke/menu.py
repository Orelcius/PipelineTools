import nuke
import CreateTicket_Nuke

menubar = nuke.menu("Nuke")
tbmenu = menubar.addMenu("Pipeline Tools")
tbmenu.addCommand("Create Helpdesk Ticket", CreateTicket_Nuke.main, "")