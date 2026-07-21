import tkinter as tk
from tkinter import ttk, messagebox
import os, sys
from datetime import date, datetime

import database as db
import reports

BG      = "#0d1b2a"
PANEL   = "#122236"
CARD    = "#162d43"
BORDER  = "#1e3a50"
ACCENT  = "#1a8fc1"
ACCENT2 = "#e8a838"
SUCCESS = "#3dba7a"
DANGER  = "#e05252"
TEXT    = "#d8eaf5"
SUBTEXT = "#6e92a8"
FONT    = ("Segoe UI", 10)
FONT_B  = ("Segoe UI", 10, "bold")
FONT_H  = ("Segoe UI", 13, "bold")
FONT_T  = ("Segoe UI", 16, "bold")

STATUS_COLOR = {
    "Scheduled":   "#2eafd4",
    "In Progress": "#e8a838",
    "Completed":   "#3dba7a",
    "Cancelled":   "#e05252",
}
PRIORITY_COLOR = {
    "Emergency": "#e05252",
    "High":      "#e8a838",
    "Normal":    "#3dba7a",
    "Low":       "#6e92a8",
}
REQUEST_COLOR = {
    "Pending":  "#e8a838",
    "Approved": "#3dba7a",
    "Rejected": "#e05252",
}


def style_app(root):
    s = ttk.Style(root)
    s.theme_use("clam")
    s.configure(".",               background=BG,    foreground=TEXT,      font=FONT)
    s.configure("TFrame",          background=BG)
    s.configure("TLabel",          background=BG,    foreground=TEXT,      font=FONT)
    s.configure("TButton",         background=ACCENT, foreground="#ffffff", font=FONT_B, padding=(12,6), relief="flat")
    s.map("TButton",               background=[("active","#137aaa")])
    s.configure("Danger.TButton",  background=DANGER,  foreground="#ffffff", font=FONT_B, padding=(12,6))
    s.map("Danger.TButton",        background=[("active","#c03a3a")])
    s.configure("Success.TButton", background=SUCCESS, foreground="#ffffff", font=FONT_B, padding=(12,6))
    s.configure("TEntry",          fieldbackground=CARD, foreground=TEXT, insertcolor=TEXT, relief="flat", font=FONT)
    s.configure("TCombobox",       fieldbackground=CARD, foreground=TEXT, selectbackground=ACCENT, font=FONT)
    s.map("TCombobox",             fieldbackground=[("readonly",CARD)])
    s.configure("Treeview",        background=CARD, foreground=TEXT, fieldbackground=CARD, rowheight=28, font=FONT)
    s.configure("Treeview.Heading",background=PANEL, foreground=ACCENT2, font=FONT_B, relief="flat")
    s.map("Treeview",              background=[("selected",ACCENT)])
    s.configure("TNotebook",       background=BG, borderwidth=0)
    s.configure("TNotebook.Tab",   background=PANEL, foreground=SUBTEXT, font=FONT_B, padding=(16,8))
    s.map("TNotebook.Tab",         background=[("selected",CARD)], foreground=[("selected",ACCENT2)])
    s.configure("TLabelframe",     background=BG, foreground=ACCENT2, bordercolor=BORDER, relief="groove")
    s.configure("TLabelframe.Label", background=BG, foreground=ACCENT2, font=FONT_B)
    s.configure("TScrollbar",      background=PANEL, troughcolor=BG, arrowcolor=SUBTEXT)
    s.configure("TSeparator",      background=BORDER)


def lbl(parent, text, **kw):
    return ttk.Label(parent, text=text, **kw)

def entry(parent, textvariable=None, width=22, **kw):
    return ttk.Entry(parent, textvariable=textvariable, width=width, **kw)

def combo(parent, values, textvariable=None, width=20, **kw):
    return ttk.Combobox(parent, values=values, textvariable=textvariable,
                        width=width, state="readonly", **kw)

def sep(parent):
    return ttk.Separator(parent, orient="horizontal")


# LOGIN ─────────────────────────────────────────────────────────────────────────────
class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Surgery Scheduling System – Login")
        self.configure(bg=BG)
        self.resizable(False, False)
        self.geometry("420x480")
        style_app(self)
        self._build()
        self._center()

    def _center(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - self.winfo_width())  // 2
        y = (self.winfo_screenheight() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")

    def _build(self):
        f = tk.Frame(self, bg=PANEL, bd=0)
        f.place(relx=.5, rely=.5, anchor="center", width=340, height=380)

        logo = tk.Frame(f, bg=ACCENT, width=70, height=70)
        logo.pack(pady=(35,0))
        logo.pack_propagate(False)
        tk.Label(logo, text="✚", font=("Segoe UI",32,"bold"),
                 bg=ACCENT, fg="white").place(relx=.5, rely=.5, anchor="center")

        tk.Label(f, text="SurgScheduler", font=FONT_T, bg=PANEL, fg=TEXT).pack(pady=(10,2))
        tk.Label(f, text="Hospital Surgery Management System",
                 font=("Segoe UI",9), bg=PANEL, fg=SUBTEXT).pack()

        sep(f).pack(fill="x", padx=30, pady=18)

        frm = tk.Frame(f, bg=PANEL)
        frm.pack(padx=30, fill="x")

        lbl(frm, "Username").pack(anchor="w")
        self.v_user = tk.StringVar()
        entry(frm, self.v_user, width=30).pack(fill="x", pady=(2,10))

        lbl(frm, "Password").pack(anchor="w")
        self.v_pass = tk.StringVar()
        e = entry(frm, self.v_pass, width=30)
        e.config(show="•")
        e.pack(fill="x", pady=(2,18))
        e.bind("<Return>", lambda _: self._login())

        ttk.Button(frm, text="Sign In", command=self._login, width=28).pack()

    def _login(self):
        user = db.authenticate(self.v_user.get().strip(), self.v_pass.get().strip())
        if user:
            self.destroy()
            MainApp(user).mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.", parent=self)

# MAIN APP─────────────────────────────────────────────────────────────────────────────
class MainApp(tk.Tk):
    def __init__(self, user: dict):
        super().__init__()
        self.user = user
        self.role = user["role"]
        self.title(f"SurgScheduler – {user['full_name']} [{self.role.title()}]")
        self.configure(bg=BG)
        self.state("zoomed")
        style_app(self)
        self._build()

    def _build(self):
        bar = tk.Frame(self, bg=PANEL, height=52)
        bar.pack(fill="x", side="top")
        tk.Label(bar, text="✚ SurgScheduler", font=("Segoe UI",14,"bold"),
                 bg=PANEL, fg=ACCENT2).pack(side="left", padx=20)

        badge_color = {"admin": ACCENT, "nurse": SUCCESS, "surgeon": "#9b59b6"}.get(self.role, SUBTEXT)
        tk.Label(bar, text=f" {self.role.upper()} ", bg=badge_color,
                 fg="white", font=FONT_B).pack(side="right", padx=6, pady=12)
        tk.Label(bar, text=self.user["full_name"], bg=PANEL, fg=TEXT, font=FONT).pack(side="right", padx=4)
        tk.Label(bar, text="👤", bg=PANEL, fg=SUBTEXT, font=("Segoe UI",14)).pack(side="right", padx=(16,2))
        ttk.Button(bar, text="Logout", command=self._logout,
                   style="Danger.TButton").pack(side="right", padx=10, pady=10)

        nb = ttk.Notebook(self)
        nb.pack(fill="both", expand=True, padx=12, pady=(8,12))

        if self.role == "admin":
            self._build_admin(nb)
        elif self.role == "nurse":
            self._build_nurse(nb)
        elif self.role == "surgeon":
            self._build_surgeon(nb)

    def _build_admin(self, nb):
        t1 = ScheduleTab(nb, self.user)
        t2 = PatientsTab(nb, self.user)
        t3 = SurgeonsTab(nb, self.user)
        t4 = EquipmentTab(nb, self.user)
        t5 = ReportsTab(nb, self.user)
        t6 = SurgeryRequestsAdminTab(nb, self.user)
        t7 = UsersTab(nb, self.user)
        nb.add(t1, text=" 📅 Schedule ")
        nb.add(t2, text=" 👥 Patients ")
        nb.add(t3, text=" 🩺 Surgeons ")
        nb.add(t4, text=" 🔧 Equipment ")
        nb.add(t5, text=" 📊 Reports ")
        nb.add(t6, text=" 📋 Requests ")
        nb.add(t7, text=" 👤 Users ")

    def _build_nurse(self, nb):
        t1 = NurseScheduleTab(nb, self.user)
        t2 = EquipmentTab(nb, self.user)
        nb.add(t1, text=" 📅 My Surgeries ")
        nb.add(t2, text=" 🔧 Equipment ")

    def _build_surgeon(self, nb):
        t1 = SurgeonScheduleTab(nb, self.user)
        t2 = SurgeryRequestSurgeonTab(nb, self.user)
        nb.add(t1, text=" 📅 My Surgeries ")
        nb.add(t2, text=" 📋 My Requests ")

    def _logout(self):
        self.destroy()
        LoginWindow().mainloop()

# HELPERS ─────────────────────────────────────────────────────────────────────────────
def make_tree(parent, cols, col_widths=None):
    frame = tk.Frame(parent, bg=BG)
    vsb = ttk.Scrollbar(frame, orient="vertical")
    hsb = ttk.Scrollbar(frame, orient="horizontal")
    tree = ttk.Treeview(frame, columns=cols, show="headings",
                        yscrollcommand=vsb.set, xscrollcommand=hsb.set,
                        selectmode="browse")
    vsb.config(command=tree.yview)
    hsb.config(command=tree.xview)
    for i, c in enumerate(cols):
        w = col_widths[i] if col_widths else 120
        tree.heading(c, text=c)
        tree.column(c, width=w, minwidth=60)
    tree.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    return frame, tree

# ADMIN SCHEDULE TAB─────────────────────────────────────────────────────────────────────────────
class ScheduleTab(ttk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user
        self._build()
        self.load()

    def _build(self):
        tb = tk.Frame(self, bg=BG)
        tb.pack(fill="x", padx=10, pady=(10,4))
        ttk.Button(tb, text="➕ Add Surgery",  command=self._add,    style="Success.TButton").pack(side="left", padx=(0,6))
        ttk.Button(tb, text="✏️ Edit Status",  command=self._status).pack(side="left", padx=6)
        ttk.Button(tb, text="👩 Assign Nurse", command=self._assign).pack(side="left", padx=6)
        ttk.Button(tb, text="🗑 Delete",        command=self._delete, style="Danger.TButton").pack(side="left", padx=6)
        ttk.Button(tb, text="🔄 Refresh",       command=self.load).pack(side="right")

        cols   = ["#","Patient","Surgeon","Type","Date","Time","Dur","Status","Priority","Room","Assigned Nurse"]
        widths = [40, 140,     130,      130,   90,   65,   60,  95,      75,       65,  130]
        frame, self.tree = make_tree(self, cols, widths)
        frame.pack(fill="both", expand=True, padx=10, pady=4)

    def load(self):
        for r in self.tree.get_children(): self.tree.delete(r)
        for i, s in enumerate(db.get_all_surgeries(), 1):
            tag = s["status"].replace(" ","_")
            self.tree.insert("","end", iid=str(s["id"]),
                             values=(i, s["patient_name"], s["surgeon_name"],
                                     s["surgery_type"], s["scheduled_date"], s["scheduled_time"],
                                     f"{s['duration_min']}m", s["status"], s["priority"],
                                     s.get("room_name","—"), s.get("assigned_nurse","—")),
                             tags=(tag,))
        for st, col in STATUS_COLOR.items():
            self.tree.tag_configure(st.replace(" ","_"), foreground=col)

    def _sel(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Select","Please select a surgery first."); return None
        return int(sel[0])

    def _add(self):    SurgeryDialog(self, self.user, callback=self.load)
    def _status(self):
        sid = self._sel()
        if sid: StatusDialog(self, sid, callback=self.load)
    def _assign(self):
        sid = self._sel()
        if sid: AssignNurseDialog(self, sid, callback=self.load)
    def _delete(self):
        sid = self._sel()
        if sid and messagebox.askyesno("Confirm", f"Delete surgery #{sid}?"):
            db.delete_surgery(sid); self.load()


# NURSE SCHEDULE TAB   ─────────────────────────────────────────────────────────────────────────────
class NurseScheduleTab(ttk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user
        self._build()
        self.load()

    def _build(self):
        tb = tk.Frame(self, bg=BG)
        tb.pack(fill="x", padx=10, pady=(10,4))
        ttk.Button(tb, text="🔄 Refresh", command=self.load).pack(side="right")
        tk.Label(self, text="Showing only surgeries assigned to you",
                 bg=BG, fg=SUBTEXT, font=("Segoe UI",9,"italic")).pack(anchor="w", padx=12)

        cols   = ["#","Patient","Surgeon","Type","Date","Time","Duration","Status","Priority","Room"]
        widths = [40, 150,     140,      130,   90,   65,   70,       95,      75,       70]
        frame, self.tree = make_tree(self, cols, widths)
        frame.pack(fill="both", expand=True, padx=10, pady=4)

    def load(self):
        for r in self.tree.get_children(): self.tree.delete(r)
        for i, s in enumerate(db.get_surgeries_for_nurse(self.user["id"]), 1):
            tag = s["status"].replace(" ","_")
            self.tree.insert("","end", iid=str(s["id"]),
                             values=(i, s["patient_name"], s["surgeon_name"],
                                     s["surgery_type"], s["scheduled_date"], s["scheduled_time"],
                                     f"{s['duration_min']} min", s["status"],
                                     s["priority"], s.get("room_name","—")),
                             tags=(tag,))
        for st, col in STATUS_COLOR.items():
            self.tree.tag_configure(st.replace(" ","_"), foreground=col)


# SURGEON SCHEDULE TAB ─────────────────────────────────────────────────────────────────────────────
class SurgeonScheduleTab(ttk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user
        self._build()
        self.load()

    def _build(self):
        tb = tk.Frame(self, bg=BG)
        tb.pack(fill="x", padx=10, pady=(10,4))

        ttk.Button(tb, text="✅ Mark as Completed",
                   command=self._mark_complete,
                   style="Success.TButton").pack(side="left", padx=(0,6))

        ttk.Button(tb, text="🔄 Refresh", command=self.load).pack(side="right")

        tk.Label(self, text="Showing only your assigned surgeries",
                 bg=BG, fg=SUBTEXT, font=("Segoe UI",9,"italic")).pack(anchor="w", padx=12)

        cols   = ["#","Patient","Type","Date","Time","Duration","Status","Priority","Room"]
        widths = [40, 150,     140,   90,   65,   70,       95,      75,       70]
        frame, self.tree = make_tree(self, cols, widths)
        frame.pack(fill="both", expand=True, padx=10, pady=4)

    def load(self):
        for r in self.tree.get_children(): self.tree.delete(r)
        for i, s in enumerate(db.get_surgeries_for_surgeon(self.user["id"]), 1):
            tag = s["status"].replace(" ","_")
            self.tree.insert("","end", iid=str(s["id"]),
                             values=(i, s["patient_name"], s["surgery_type"],
                                     s["scheduled_date"], s["scheduled_time"],
                                     f"{s['duration_min']} min", s["status"],
                                     s["priority"], s.get("room_name","—")),
                             tags=(tag,))
        for st, col in STATUS_COLOR.items():
            self.tree.tag_configure(st.replace(" ","_"), foreground=col)

    def _sel(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Select", "Please select a surgery first.")
            return None
        return int(sel[0])

    def _mark_complete(self):
        sid = self._sel()
        if sid is None:
            return
        conn = db.get_connection()
        row  = conn.execute("SELECT status FROM surgeries WHERE id=?", (sid,)).fetchone()
        conn.close()
        if row and row["status"] == "Completed":
            messagebox.showinfo("Already Done", "This surgery is already marked as Completed.")
            return
        if messagebox.askyesno("Confirm", "Mark this surgery as Completed?"):
            db.update_surgery_status(sid, "Completed")
            self.load()
            messagebox.showinfo("Updated", "Surgery marked as Completed ✅")


# ─────────────────────────────────────────────────────────────────────────────
# ASSIGN NURSE DIALOG
# ─────────────────────────────────────────────────────────────────────────────
class AssignNurseDialog(tk.Toplevel):
    def __init__(self, parent, surgery_id, callback=None):
        super().__init__(parent)
        self.title("Assign Nurse to Surgery")
        self.configure(bg=BG)
        self.resizable(False, False)
        self.grab_set()
        self.surgery_id = surgery_id
        self.callback   = callback
        self._build()
        self._center()

    def _center(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - self.winfo_width())  // 2
        y = (self.winfo_screenheight() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")

    def _build(self):
        f = tk.Frame(self, bg=BG, padx=30, pady=24)
        f.pack(fill="both", expand=True)

        tk.Label(f, text=f"Assign Nurse — Surgery #{self.surgery_id}",
                 font=FONT_H, bg=BG, fg=ACCENT2).pack(pady=(0,14))

        nurses = db.get_all_nurses()
        self.nurse_map = {n["full_name"]: n["id"] for n in nurses}

        current      = db.get_assignment_for_surgery(self.surgery_id)
        current_name = current["full_name"] if current else ""

        lbl(f, "Select Nurse:").pack(anchor="w")
        self.v_nurse = tk.StringVar(value=current_name)
        combo(f, list(self.nurse_map.keys()), self.v_nurse, 30).pack(fill="x", pady=(4,16))

        sep(f).pack(fill="x", pady=8)

        bf = tk.Frame(f, bg=BG)
        bf.pack(anchor="e")
        ttk.Button(bf, text="Cancel", command=self.destroy).pack(side="right", padx=(6,0))
        ttk.Button(bf, text="Assign", command=self._save,
                   style="Success.TButton").pack(side="right")

    def _save(self):
        name = self.v_nurse.get()
        if not name or name not in self.nurse_map:
            messagebox.showerror("Error","Please select a nurse.", parent=self); return
        db.assign_nurse_to_surgery(self.surgery_id, self.nurse_map[name])
        messagebox.showinfo("Done", f"Nurse assigned to surgery #{self.surgery_id}!", parent=self)
        if self.callback: self.callback()
        self.destroy()


# ─────────────────────────────────────────────────────────────────────────────
# SURGERY REQUEST TABS
# ─────────────────────────────────────────────────────────────────────────────
class SurgeryRequestSurgeonTab(ttk.Frame):
    """Surgeon view: submit requests, see status, delete pending ones."""
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user
        self._build()
        self.load()

    def _build(self):
        tb = tk.Frame(self, bg=BG)
        tb.pack(fill="x", padx=10, pady=(10,4))
        ttk.Button(tb, text="➕ New Request", command=self._add,
                   style="Success.TButton").pack(side="left", padx=(0,6))

        ttk.Button(tb, text="🗑 Delete Request", command=self._delete,
                   style="Danger.TButton").pack(side="left", padx=6)

        ttk.Button(tb, text="🔄 Refresh", command=self.load).pack(side="right")

        # Status legend
        legend = tk.Frame(self, bg=BG)
        legend.pack(anchor="w", padx=12, pady=(0,4))
        for status, color in REQUEST_COLOR.items():
            tk.Label(legend, text=f"● {status}", fg=color, bg=BG,
                     font=("Segoe UI",9)).pack(side="left", padx=6)

        cols   = ["#","Patient","Surgery Type","Pref. Date","Pref. Time","Priority","Status","Admin Notes"]
        widths = [40, 140,     140,           90,          70,          70,       80,      200]
        frame, self.tree = make_tree(self, cols, widths)
        frame.pack(fill="both", expand=True, padx=10, pady=4)

    def load(self):
        for r in self.tree.get_children(): self.tree.delete(r)
        for i, req in enumerate(db.get_surgery_requests_for_surgeon(self.user["id"]), 1):
            tag = req["status"]
            self.tree.insert("","end", iid=str(req["id"]),
                             values=(i, req["patient_name"], req["surgery_type"],
                                     req["preferred_date"], req["preferred_time"],
                                     req["priority"], req["status"],
                                     req.get("admin_notes","—")),
                             tags=(tag,))
        for st, col in REQUEST_COLOR.items():
            self.tree.tag_configure(st, foreground=col)

    def _sel(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Select", "Please select a request first.")
            return None
        return int(sel[0])

    def _add(self):
        SurgeryRequestDialog(self, self.user, callback=self.load)

    def _delete(self):
        rid = self._sel()
        if rid is None:
            return
        conn = db.get_connection()
        row  = conn.execute(
            "SELECT status FROM surgery_requests WHERE id=?", (rid,)
        ).fetchone()
        conn.close()

        if row is None:
            messagebox.showerror("Error", "Request not found."); return

        if row["status"] != "Pending":
            messagebox.showerror(
                "Cannot Delete",
                f"Only Pending requests can be deleted.\n"
                f"This request is already '{row['status']}'."
            )
            return

        if messagebox.askyesno("Confirm", "Delete this pending request?"):
            db.delete_surgery_request(rid)
            self.load()


class SurgeryRequestsAdminTab(ttk.Frame):
    """Admin view: see all requests, approve or reject."""
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user
        self._build()
        self.load()

    def _build(self):
        tb = tk.Frame(self, bg=BG)
        tb.pack(fill="x", padx=10, pady=(10,4))
        ttk.Button(tb, text="✅ Approve", command=self._approve,
                   style="Success.TButton").pack(side="left", padx=(0,6))
        ttk.Button(tb, text="❌ Reject",  command=self._reject,
                   style="Danger.TButton").pack(side="left", padx=6)
        ttk.Button(tb, text="🔄 Refresh", command=self.load).pack(side="right")

        cols   = ["#","Surgeon","Patient","Surgery Type","Pref. Date","Pref. Time","Priority","Status","Notes"]
        widths = [40, 130,     130,      130,           90,          70,          70,       80,      180]
        frame, self.tree = make_tree(self, cols, widths)
        frame.pack(fill="both", expand=True, padx=10, pady=4)

    def load(self):
        for r in self.tree.get_children(): self.tree.delete(r)
        for i, req in enumerate(db.get_all_surgery_requests(), 1):
            tag = req["status"]
            self.tree.insert("","end", iid=str(req["id"]),
                             values=(i, req["surgeon_name"], req["patient_name"],
                                     req["surgery_type"], req["preferred_date"], req["preferred_time"],
                                     req["priority"], req["status"], req.get("notes","—")),
                             tags=(tag,))
        for st, col in REQUEST_COLOR.items():
            self.tree.tag_configure(st, foreground=col)

    def _sel(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Select","Please select a request."); return None
        return int(sel[0])

    def _approve(self):
        rid = self._sel()
        if rid is None: return
        conn = db.get_connection()
        row  = conn.execute("SELECT status FROM surgery_requests WHERE id=?", (rid,)).fetchone()
        conn.close()
        if row and row["status"] == "Approved":
            messagebox.showinfo("Already Approved", "This request is already approved."); return
        AdminReviewDialog(self, rid, "Approved", callback=self.load)

    def _reject(self):
        rid = self._sel()
        if rid is None: return
        AdminReviewDialog(self, rid, "Rejected", callback=self.load)


class SurgeryRequestDialog(tk.Toplevel):
    """Surgeon fills out a surgery request form."""
    def __init__(self, parent, user, callback=None):
        super().__init__(parent)
        self.title("Request Surgery")
        self.configure(bg=BG)
        self.resizable(False, False)
        self.grab_set()
        self.user     = user
        self.callback = callback
        self._build()
        self._center()

    def _center(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - self.winfo_width())  // 2
        y = (self.winfo_screenheight() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")

    def _build(self):
        f = tk.Frame(self, bg=BG, padx=24, pady=20)
        f.pack(fill="both", expand=True)

        tk.Label(f, text="Surgery Request", font=FONT_H, bg=BG, fg=ACCENT2).grid(
            row=0, column=0, columnspan=2, pady=(0,16), sticky="w")

        lbl(f,"Patient Name *").grid(row=1,column=0,sticky="w",pady=3)
        self.v_patient = tk.StringVar()
        entry(f, self.v_patient, 32).grid(row=1,column=1,sticky="ew",pady=3)

        types = ["Appendectomy","Bypass Surgery","Cataract Removal","Colectomy",
                 "Hip Replacement","Knee Replacement","Laparoscopy","Mastectomy",
                 "Spinal Fusion","Tonsillectomy","Other"]
        lbl(f,"Surgery Type *").grid(row=2,column=0,sticky="w",pady=3)
        self.v_type = tk.StringVar()
        combo(f, types, self.v_type, 30).grid(row=2,column=1,sticky="ew",pady=3)

        lbl(f,"Preferred Date * (YYYY-MM-DD)").grid(row=3,column=0,sticky="w",pady=3)
        self.v_date = tk.StringVar(value=str(date.today()))
        entry(f, self.v_date, 30).grid(row=3,column=1,sticky="ew",pady=3)

        lbl(f,"Preferred Time * (HH:MM)").grid(row=4,column=0,sticky="w",pady=3)
        self.v_time = tk.StringVar(value="08:00")
        entry(f, self.v_time, 30).grid(row=4,column=1,sticky="ew",pady=3)

        lbl(f,"Duration (minutes)").grid(row=5,column=0,sticky="w",pady=3)
        self.v_dur = tk.StringVar(value="60")
        entry(f, self.v_dur, 30).grid(row=5,column=1,sticky="ew",pady=3)

        lbl(f,"Priority").grid(row=6,column=0,sticky="w",pady=3)
        self.v_priority = tk.StringVar(value="Normal")
        combo(f,["Emergency","High","Normal","Low"],self.v_priority,30).grid(
            row=6,column=1,sticky="ew",pady=3)

        lbl(f,"Notes").grid(row=7,column=0,sticky="nw",pady=3)
        self.txt = tk.Text(f, width=32, height=3, bg=CARD, fg=TEXT,
                           insertbackground=TEXT, relief="flat", font=FONT)
        self.txt.grid(row=7,column=1,sticky="ew",pady=3)

        sep(f).grid(row=8,column=0,columnspan=2,sticky="ew",pady=12)

        bf = tk.Frame(f, bg=BG)
        bf.grid(row=9,column=0,columnspan=2,sticky="e")
        ttk.Button(bf,text="Cancel",command=self.destroy).pack(side="right",padx=(6,0))
        ttk.Button(bf,text="Submit Request",command=self._save,
                   style="Success.TButton").pack(side="right")

    def _save(self):
        patient = self.v_patient.get().strip()
        stype   = self.v_type.get()
        pdate   = self.v_date.get().strip()
        ptime   = self.v_time.get().strip()
        if not patient or not stype or not pdate or not ptime:
            messagebox.showerror("Validation","All starred fields are required.", parent=self)
            return
        try:
            dur = int(self.v_dur.get())
        except Exception:
            dur = 60

        conn = db.get_connection()
        sg   = conn.execute("SELECT id FROM surgeons WHERE user_id=?",
                            (self.user["id"],)).fetchone()
        conn.close()
        if not sg:
            messagebox.showerror("Error",
                "Your account is not linked to a surgeon profile. Ask admin to link it.",
                parent=self)
            return

        db.add_surgery_request({
            "surgeon_id":     sg["id"],
            "patient_name":   patient,
            "surgery_type":   stype,
            "preferred_date": pdate,
            "preferred_time": ptime,
            "duration_min":   dur,
            "priority":       self.v_priority.get(),
            "notes":          self.txt.get("1.0","end").strip(),
        })
        messagebox.showinfo("Submitted","Your surgery request has been sent to admin!", parent=self)
        if self.callback: self.callback()
        self.destroy()


class AdminReviewDialog(tk.Toplevel):
    """Admin approves or rejects a surgery request with optional notes."""
    def __init__(self, parent, request_id, action, callback=None):
        super().__init__(parent)
        self.title(f"{action} Request")
        self.configure(bg=BG)
        self.resizable(False, False)
        self.grab_set()
        self.request_id = request_id
        self.action     = action
        self.callback   = callback

        f = tk.Frame(self, bg=BG, padx=30, pady=24)
        f.pack(fill="both", expand=True)

        color = SUCCESS if action == "Approved" else DANGER
        tk.Label(f, text=f"{action} Request #{request_id}",
                 font=FONT_H, bg=BG, fg=color).pack(pady=(0,12))

        lbl(f,"Notes for surgeon (optional):").pack(anchor="w")
        self.txt = tk.Text(f, width=36, height=4, bg=CARD, fg=TEXT,
                           insertbackground=TEXT, relief="flat", font=FONT)
        self.txt.pack(fill="x", pady=(4,14))

        sep(f).pack(fill="x", pady=8)

        bf = tk.Frame(f, bg=BG)
        bf.pack(anchor="e")
        ttk.Button(bf,text="Cancel",command=self.destroy).pack(side="right",padx=(6,0))
        style = "Success.TButton" if action == "Approved" else "Danger.TButton"
        ttk.Button(bf, text=action, command=self._save, style=style).pack(side="right")

    def _save(self):
        notes = self.txt.get("1.0","end").strip()
        db.update_surgery_request_status(self.request_id, self.action, notes)
        messagebox.showinfo("Done", f"Request #{self.request_id} marked as {self.action}.")
        if self.callback: self.callback()
        self.destroy()


# ─────────────────────────────────────────────────────────────────────────────
# SURGERY ADD DIALOG
# ─────────────────────────────────────────────────────────────────────────────
class SurgeryDialog(tk.Toplevel):
    def __init__(self, parent, user, callback=None):
        super().__init__(parent)
        self.title("Schedule New Surgery")
        self.configure(bg=BG)
        self.resizable(False, False)
        self.grab_set()
        self.user     = user
        self.callback = callback
        self._build()
        self._center()

    def _center(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - self.winfo_width())  // 2
        y = (self.winfo_screenheight() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")

    def _build(self):
        f = tk.Frame(self, bg=BG, padx=24, pady=20)
        f.pack(fill="both", expand=True)

        tk.Label(f, text="Schedule New Surgery", font=FONT_H, bg=BG, fg=ACCENT2).grid(
            row=0,column=0,columnspan=2,pady=(0,16),sticky="w")

        patients = db.get_all_patients()
        self.patient_map = {p["name"]: p["id"] for p in patients}
        lbl(f,"Patient *").grid(row=1,column=0,sticky="w",pady=3)
        self.v_patient = tk.StringVar()
        combo(f,list(self.patient_map),self.v_patient,30).grid(row=1,column=1,sticky="ew",pady=3)

        surgeons = db.get_all_surgeons()
        self.surgeon_map = {s["name"]: s["id"] for s in surgeons}
        lbl(f,"Surgeon *").grid(row=2,column=0,sticky="w",pady=3)
        self.v_surgeon = tk.StringVar()
        combo(f,list(self.surgeon_map),self.v_surgeon,30).grid(row=2,column=1,sticky="ew",pady=3)

        nurses = db.get_all_nurses()
        self.nurse_map = {"None": None}
        self.nurse_map.update({n["full_name"]: n["id"] for n in nurses})
        lbl(f,"Assign Nurse").grid(row=3,column=0,sticky="w",pady=3)
        self.v_nurse = tk.StringVar(value="None")
        combo(f,list(self.nurse_map.keys()),self.v_nurse,30).grid(row=3,column=1,sticky="ew",pady=3)

        conn = db.get_connection()
        rooms = conn.execute("SELECT * FROM operating_rooms").fetchall()
        conn.close()
        self.room_map = {"None / TBD": None}
        self.room_map.update({r["name"]: r["id"] for r in rooms})
        lbl(f,"Operating Room").grid(row=4,column=0,sticky="w",pady=3)
        self.v_room = tk.StringVar(value="None / TBD")
        combo(f,list(self.room_map),self.v_room,30).grid(row=4,column=1,sticky="ew",pady=3)

        types = ["Appendectomy","Bypass Surgery","Cataract Removal","Colectomy",
                 "Hip Replacement","Knee Replacement","Laparoscopy","Mastectomy",
                 "Spinal Fusion","Tonsillectomy","Other"]
        lbl(f,"Surgery Type *").grid(row=5,column=0,sticky="w",pady=3)
        self.v_type = tk.StringVar()
        combo(f,types,self.v_type,30).grid(row=5,column=1,sticky="ew",pady=3)

        lbl(f,"Date * (YYYY-MM-DD)").grid(row=6,column=0,sticky="w",pady=3)
        self.v_date = tk.StringVar(value=str(date.today()))
        entry(f,self.v_date,30).grid(row=6,column=1,sticky="ew",pady=3)

        lbl(f,"Time * (HH:MM)").grid(row=7,column=0,sticky="w",pady=3)
        self.v_time = tk.StringVar(value="08:00")
        entry(f,self.v_time,30).grid(row=7,column=1,sticky="ew",pady=3)

        lbl(f,"Duration (minutes)").grid(row=8,column=0,sticky="w",pady=3)
        self.v_dur = tk.StringVar(value="60")
        entry(f,self.v_dur,30).grid(row=8,column=1,sticky="ew",pady=3)

        lbl(f,"Priority").grid(row=9,column=0,sticky="w",pady=3)
        self.v_priority = tk.StringVar(value="Normal")
        combo(f,["Emergency","High","Normal","Low"],self.v_priority,30).grid(
            row=9,column=1,sticky="ew",pady=3)

        lbl(f,"Notes").grid(row=10,column=0,sticky="nw",pady=3)
        self.txt_notes = tk.Text(f,width=32,height=3,bg=CARD,fg=TEXT,
                                 insertbackground=TEXT,relief="flat",font=FONT)
        self.txt_notes.grid(row=10,column=1,sticky="ew",pady=3)

        sep(f).grid(row=11,column=0,columnspan=2,sticky="ew",pady=12)

        bf = tk.Frame(f, bg=BG)
        bf.grid(row=12,column=0,columnspan=2,sticky="e")
        ttk.Button(bf,text="Cancel",command=self.destroy).pack(side="right",padx=(6,0))
        ttk.Button(bf,text="Schedule Surgery",command=self._save,
                   style="Success.TButton").pack(side="right")

    def _save(self):
        for name, val in [("Patient",self.v_patient.get()),("Surgeon",self.v_surgeon.get()),
                           ("Surgery Type",self.v_type.get()),("Date",self.v_date.get()),
                           ("Time",self.v_time.get())]:
            if not val:
                messagebox.showerror("Validation",f"{name} is required.",parent=self); return
        try:
            dur = int(self.v_dur.get())
        except ValueError:
            messagebox.showerror("Validation","Duration must be a number.",parent=self); return

        data = {
            "patient_id":     self.patient_map[self.v_patient.get()],
            "surgeon_id":     self.surgeon_map[self.v_surgeon.get()],
            "room_id":        self.room_map[self.v_room.get()],
            "surgery_type":   self.v_type.get(),
            "scheduled_date": self.v_date.get(),
            "scheduled_time": self.v_time.get(),
            "duration_min":   dur,
            "status":         "Scheduled",
            "priority":       self.v_priority.get(),
            "notes":          self.txt_notes.get("1.0","end").strip(),
            "created_by":     self.user["id"],
        }
        surgery_id = db.add_surgery(data)

        nurse_name = self.v_nurse.get()
        if nurse_name and nurse_name != "None":
            db.assign_nurse_to_surgery(surgery_id, self.nurse_map[nurse_name])

        messagebox.showinfo("Success","Surgery scheduled successfully!", parent=self)
        if self.callback: self.callback()
        self.destroy()


class StatusDialog(tk.Toplevel):
    def __init__(self, parent, surgery_id, callback=None):
        super().__init__(parent)
        self.title("Update Surgery Status")
        self.configure(bg=BG)
        self.resizable(False, False)
        self.grab_set()
        self.surgery_id = surgery_id
        self.callback   = callback
        f = tk.Frame(self, bg=BG, padx=30, pady=24)
        f.pack()
        lbl(f, f"Surgery #{surgery_id} — New Status:", font=FONT_B).pack(pady=(0,10))
        self.v = tk.StringVar(value="Scheduled")
        for s in ["Scheduled","In Progress","Completed","Cancelled"]:
            tk.Radiobutton(f, text=s, variable=self.v, value=s, bg=BG,
                           fg=STATUS_COLOR[s], selectcolor=CARD,
                           activebackground=BG, font=FONT_B).pack(anchor="w", pady=2)
        sep(f).pack(fill="x", pady=12)
        ttk.Button(f, text="Update", command=self._save, style="Success.TButton").pack()

    def _save(self):
        db.update_surgery_status(self.surgery_id, self.v.get())
        if self.callback: self.callback()
        self.destroy()


# ─────────────────────────────────────────────────────────────────────────────
# PATIENTS TAB
# ─────────────────────────────────────────────────────────────────────────────
class PatientsTab(ttk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user     = user
        self.is_admin = user["role"] == "admin"
        self._build()
        self.load()

    def _build(self):
        tb = tk.Frame(self, bg=BG)
        tb.pack(fill="x", padx=10, pady=(10,4))
        ttk.Button(tb,text="➕ Add Patient",command=self._add,
                   style="Success.TButton").pack(side="left",padx=(0,6))
        ttk.Button(tb,text="✏️ Edit",command=self._edit).pack(side="left",padx=6)
        if self.is_admin:
            ttk.Button(tb,text="🗑 Delete",command=self._delete,
                       style="Danger.TButton").pack(side="left",padx=6)
        ttk.Button(tb,text="🔄",command=self.load).pack(side="right")

        cols   = ["#","Name","DOB","Gender","Phone","Blood Type","Allergies"]
        widths = [40, 160,   90,   70,      110,    80,          180]
        frame, self.tree = make_tree(self, cols, widths)
        frame.pack(fill="both", expand=True, padx=10, pady=4)

    def load(self):
        for r in self.tree.get_children(): self.tree.delete(r)
        for i, p in enumerate(db.get_all_patients(), 1):
            self.tree.insert("","end", iid=str(p["id"]),
                             values=(i, p["name"], p.get("dob",""), p.get("gender",""),
                                     p.get("phone",""), p.get("blood_type",""), p.get("allergies","")))

    def _sel(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Select","Please select a patient."); return None
        return int(sel[0])

    def _add(self): PatientDialog(self, callback=self.load)
    def _edit(self):
        pid = self._sel()
        if pid is None: return
        conn = db.get_connection()
        row  = conn.execute("SELECT * FROM patients WHERE id=?",(pid,)).fetchone()
        conn.close()
        PatientDialog(self, data=dict(row), callback=self.load)
    def _delete(self):
        pid = self._sel()
        if pid is None: return
        if messagebox.askyesno("Confirm","Delete this patient?"):
            db.delete_patient(pid); self.load()


class PatientDialog(tk.Toplevel):
    def __init__(self, parent, data=None, callback=None):
        super().__init__(parent)
        self.title("Patient" if data else "New Patient")
        self.configure(bg=BG)
        self.resizable(False, False)
        self.grab_set()
        self.data     = data
        self.callback = callback
        self._build()
        self._center()
        if data: self._fill()

    def _center(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - self.winfo_width())  // 2
        y = (self.winfo_screenheight() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")

    def _build(self):
        f = tk.Frame(self,bg=BG,padx=24,pady=20); f.pack(fill="both",expand=True)
        tk.Label(f,text="Patient Information",font=FONT_H,bg=BG,fg=ACCENT2).grid(
            row=0,column=0,columnspan=2,pady=(0,14),sticky="w")
        fields = [("Full Name *","v_name"),("Date of Birth (YYYY-MM-DD)","v_dob"),
                  ("Blood Type","v_blood"),("Phone","v_phone"),("Allergies","v_allergies")]
        for i,(label,var) in enumerate(fields,1):
            lbl(f,label).grid(row=i,column=0,sticky="w",pady=3)
            setattr(self,var,tk.StringVar())
            entry(f,getattr(self,var),32).grid(row=i,column=1,sticky="ew",pady=3)
        lbl(f,"Gender").grid(row=6,column=0,sticky="w",pady=3)
        self.v_gender = tk.StringVar(value="Male")
        combo(f,["Male","Female","Other"],self.v_gender,30).grid(row=6,column=1,sticky="ew",pady=3)
        lbl(f,"Notes").grid(row=7,column=0,sticky="nw",pady=3)
        self.txt = tk.Text(f,width=32,height=3,bg=CARD,fg=TEXT,
                           insertbackground=TEXT,relief="flat",font=FONT)
        self.txt.grid(row=7,column=1,sticky="ew",pady=3)
        sep(f).grid(row=8,column=0,columnspan=2,sticky="ew",pady=10)
        bf = tk.Frame(f,bg=BG); bf.grid(row=9,column=0,columnspan=2,sticky="e")
        ttk.Button(bf,text="Cancel",command=self.destroy).pack(side="right",padx=(6,0))
        ttk.Button(bf,text="Save",command=self._save,style="Success.TButton").pack(side="right")

    def _fill(self):
        d = self.data
        self.v_name.set(d.get("name","")); self.v_dob.set(d.get("dob",""))
        self.v_blood.set(d.get("blood_type","")); self.v_phone.set(d.get("phone",""))
        self.v_allergies.set(d.get("allergies","")); self.v_gender.set(d.get("gender","Male"))
        self.txt.insert("1.0",d.get("notes",""))

    def _save(self):
        if not self.v_name.get().strip():
            messagebox.showerror("Validation","Name is required.",parent=self); return
        data = dict(name=self.v_name.get().strip(), dob=self.v_dob.get(),
                    gender=self.v_gender.get(), phone=self.v_phone.get(),
                    blood_type=self.v_blood.get(), allergies=self.v_allergies.get(),
                    notes=self.txt.get("1.0","end").strip())
        if self.data:
            data["id"] = self.data["id"]; db.update_patient(data)
        else:
            db.add_patient(data)
        if self.callback: self.callback()
        self.destroy()


# ─────────────────────────────────────────────────────────────────────────────
# SURGEONS TAB
# ─────────────────────────────────────────────────────────────────────────────
class SurgeonsTab(ttk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user
        self._build()
        self.load()

    def _build(self):
        tb = tk.Frame(self, bg=BG)
        tb.pack(fill="x", padx=10, pady=(10,4))
        ttk.Button(tb,text="➕ Add Surgeon",command=self._add,
                   style="Success.TButton").pack(side="left",padx=(0,6))
        ttk.Button(tb,text="✏️ Edit",command=self._edit).pack(side="left",padx=6)
        ttk.Button(tb,text="🗑 Delete",command=self._delete,
                   style="Danger.TButton").pack(side="left",padx=6)
        # Fix 4: Link User button
        ttk.Button(tb, text="🔗 Link User", command=self._link_user).pack(side="left", padx=6)
        ttk.Button(tb,text="🔄",command=self.load).pack(side="right")

        cols   = ["#","Name","Specialty","Phone","Email","Available"]
        widths = [40, 160,   140,       110,    200,    80]
        frame, self.tree = make_tree(self, cols, widths)
        frame.pack(fill="both", expand=True, padx=10, pady=4)

    def load(self):
        for r in self.tree.get_children(): self.tree.delete(r)
        for i, s in enumerate(db.get_all_surgeons(), 1):
            avail = "✅ Yes" if s["available"] else "❌ No"
            self.tree.insert("","end", iid=str(s["id"]),
                             values=(i, s["name"], s["specialty"],
                                     s.get("phone",""), s.get("email",""), avail))

    def _sel(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Select","Please select a surgeon."); return None
        return int(sel[0])

    def _add(self): SurgeonDialog(self, callback=self.load)
    def _edit(self):
        sid = self._sel()
        if sid is None: return
        conn = db.get_connection()
        row  = conn.execute("SELECT * FROM surgeons WHERE id=?",(sid,)).fetchone()
        conn.close()
        SurgeonDialog(self, data=dict(row), callback=self.load)

    def _delete(self):
        sid = self._sel()
        if sid is None: return
        if messagebox.askyesno("Confirm", "Delete this surgeon?"):
            try:
                db.delete_surgeon(sid)
                self.load()
            except Exception as e:
                messagebox.showerror("Cannot Delete", str(e))

    # Fix 4: _link_user method
    def _link_user(self):
        sid = self._sel()
        if sid is None: return
        conn = db.get_connection()
        users = conn.execute(
            "SELECT id, full_name FROM users WHERE role='surgeon' ORDER BY full_name"
        ).fetchall()
        conn.close()
        if not users:
            messagebox.showinfo("No Surgeons", "No surgeon user accounts exist yet. Create one in the Users tab.")
            return
        user_map = {u["full_name"]: u["id"] for u in users}
        LinkUserToSurgeonDialog(self, sid, user_map, callback=self.load)


class SurgeonDialog(tk.Toplevel):
    def __init__(self, parent, data=None, callback=None):
        super().__init__(parent)
        self.title("Surgeon")
        self.configure(bg=BG)
        self.resizable(False, False)
        self.grab_set()
        self.data     = data
        self.callback = callback
        self._build()
        self._center()
        if data: self._fill()

    def _center(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - self.winfo_width())  // 2
        y = (self.winfo_screenheight() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")

    def _build(self):
        f = tk.Frame(self,bg=BG,padx=24,pady=20); f.pack(fill="both",expand=True)
        tk.Label(f,text="Surgeon Information",font=FONT_H,bg=BG,fg=ACCENT2).grid(
            row=0,column=0,columnspan=2,pady=(0,14),sticky="w")
        specs = ["Cardiothoracic","General Surgery","Neurosurgery","Orthopedics",
                 "Plastic Surgery","Urology","Vascular","Other"]
        fields = [("Full Name *","v_name",None),("Specialty *","v_spec",specs),
                  ("Phone","v_phone",None),("Email","v_email",None)]
        for i,(label,var,vals) in enumerate(fields,1):
            lbl(f,label).grid(row=i,column=0,sticky="w",pady=3)
            setattr(self,var,tk.StringVar())
            if vals:
                combo(f,vals,getattr(self,var),30).grid(row=i,column=1,sticky="ew",pady=3)
            else:
                entry(f,getattr(self,var),32).grid(row=i,column=1,sticky="ew",pady=3)
        lbl(f,"Available").grid(row=5,column=0,sticky="w",pady=3)
        self.v_avail = tk.IntVar(value=1)
        tk.Checkbutton(f,variable=self.v_avail,bg=BG,fg=TEXT,
                       selectcolor=CARD,activebackground=BG).grid(row=5,column=1,sticky="w")
        sep(f).grid(row=6,column=0,columnspan=2,sticky="ew",pady=10)
        bf = tk.Frame(f,bg=BG); bf.grid(row=7,column=0,columnspan=2,sticky="e")
        ttk.Button(bf,text="Cancel",command=self.destroy).pack(side="right",padx=(6,0))
        ttk.Button(bf,text="Save",command=self._save,style="Success.TButton").pack(side="right")

    def _fill(self):
        d = self.data
        self.v_name.set(d.get("name","")); self.v_spec.set(d.get("specialty",""))
        self.v_phone.set(d.get("phone","")); self.v_email.set(d.get("email",""))
        self.v_avail.set(d.get("available",1))

    def _save(self):
        if not self.v_name.get().strip() or not self.v_spec.get():
            messagebox.showerror("Validation","Name and Specialty required.",parent=self); return
        data = dict(name=self.v_name.get().strip(), specialty=self.v_spec.get(),
                    phone=self.v_phone.get(), email=self.v_email.get(),
                    available=self.v_avail.get())
        if self.data:
            data["id"] = self.data["id"]; db.update_surgeon(data)
        else:
            db.add_surgeon(data)
        if self.callback: self.callback()
        self.destroy()


# ─────────────────────────────────────────────────────────────────────────────
# EQUIPMENT TAB
# ─────────────────────────────────────────────────────────────────────────────
class EquipmentTab(ttk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user     = user
        self.is_admin = user["role"] == "admin"
        self.is_nurse = user["role"] == "nurse"
        self._build()
        self.load()

    def _build(self):
        tb = tk.Frame(self, bg=BG)
        tb.pack(fill="x", padx=10, pady=(10,4))
        if self.is_admin:
            ttk.Button(tb,text="➕ Add Equipment",command=self._add,
                       style="Success.TButton").pack(side="left",padx=(0,6))
            ttk.Button(tb,text="🗑 Delete",command=self._delete,
                       style="Danger.TButton").pack(side="left",padx=6)
        ttk.Button(tb,text="Toggle Availability",command=self._toggle_avail).pack(side="left",padx=6)
        ttk.Button(tb,text="🧪 Toggle Sterilized",command=self._toggle_sterilized).pack(side="left",padx=6)
        ttk.Button(tb,text="🔄",command=self.load).pack(side="right")

        cols   = ["#","Name","Category","Qty","Available","Sterilized","Last Service","Notes"]
        widths = [40, 170,   120,       50,   80,         90,          110,           180]
        frame, self.tree = make_tree(self, cols, widths)
        frame.pack(fill="both", expand=True, padx=10, pady=4)

    def load(self):
        for r in self.tree.get_children(): self.tree.delete(r)
        for i, e in enumerate(db.get_all_equipment(), 1):
            avail  = "✅" if e["available"]        else "❌"
            steril = "✅" if e.get("sterilized",0) else "❌"
            self.tree.insert("","end", iid=str(e["id"]),
                             values=(i, e["name"], e["category"], e["quantity"],
                                     avail, steril, e.get("last_service",""), e.get("notes","")))

    def _sel(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Select","Select an equipment item."); return None
        return int(sel[0])

    def _add(self): EquipmentDialog(self, callback=self.load)

    def _delete(self):
        eid = self._sel()
        if eid is None: return
        if messagebox.askyesno("Confirm","Delete this equipment?"):
            conn = db.get_connection()
            conn.execute("DELETE FROM equipment WHERE id=?",(eid,))
            conn.commit(); conn.close()
            self.load()

    def _toggle_avail(self):
        eid = self._sel()
        if eid is None: return
        conn = db.get_connection()
        row  = conn.execute("SELECT available FROM equipment WHERE id=?",(eid,)).fetchone()
        conn.close()
        db.update_equipment_availability(eid, 0 if row["available"] else 1)
        self.load()

    def _toggle_sterilized(self):
        eid = self._sel()
        if eid is None: return
        conn = db.get_connection()
        row  = conn.execute("SELECT sterilized FROM equipment WHERE id=?",(eid,)).fetchone()
        conn.close()
        db.update_equipment_sterilized(eid, 0 if row["sterilized"] else 1)
        self.load()


class EquipmentDialog(tk.Toplevel):
    def __init__(self, parent, callback=None):
        super().__init__(parent)
        self.title("Add Equipment")
        self.configure(bg=BG)
        self.resizable(False, False)
        self.grab_set()
        self.callback = callback
        self._build()
        self._center()

    def _center(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - self.winfo_width())  // 2
        y = (self.winfo_screenheight() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")

    def _build(self):
        f = tk.Frame(self,bg=BG,padx=24,pady=20); f.pack(fill="both",expand=True)
        tk.Label(f,text="Add Equipment",font=FONT_H,bg=BG,fg=ACCENT2).grid(
            row=0,column=0,columnspan=2,pady=(0,14),sticky="w")
        lbl(f,"Name *").grid(row=1,column=0,sticky="w",pady=3)
        self.v_name = tk.StringVar()
        entry(f,self.v_name,32).grid(row=1,column=1,sticky="ew",pady=3)
        lbl(f,"Category *").grid(row=2,column=0,sticky="w",pady=3)
        self.v_cat = tk.StringVar()
        combo(f,["Anesthesia","Robotics","Cauterization","Imaging",
                 "Laparoscopy","Respiratory","Other"],self.v_cat,30).grid(
            row=2,column=1,sticky="ew",pady=3)
        lbl(f,"Quantity").grid(row=3,column=0,sticky="w",pady=3)
        self.v_qty = tk.StringVar(value="1")
        entry(f,self.v_qty,32).grid(row=3,column=1,sticky="ew",pady=3)
        lbl(f,"Notes").grid(row=4,column=0,sticky="nw",pady=3)
        self.txt = tk.Text(f,width=32,height=3,bg=CARD,fg=TEXT,
                           insertbackground=TEXT,relief="flat",font=FONT)
        self.txt.grid(row=4,column=1,sticky="ew",pady=3)
        sep(f).grid(row=5,column=0,columnspan=2,sticky="ew",pady=10)
        bf = tk.Frame(f,bg=BG); bf.grid(row=6,column=0,columnspan=2,sticky="e")
        ttk.Button(bf,text="Cancel",command=self.destroy).pack(side="right",padx=(6,0))
        ttk.Button(bf,text="Save",command=self._save,style="Success.TButton").pack(side="right")

    def _save(self):
        if not self.v_name.get().strip() or not self.v_cat.get():
            messagebox.showerror("Validation","Name and Category required.",parent=self); return
        try: qty = int(self.v_qty.get())
        except Exception: qty = 1
        conn = db.get_connection()
        conn.execute("INSERT INTO equipment (name,category,quantity,notes) VALUES (?,?,?,?)",
                     (self.v_name.get().strip(), self.v_cat.get(), qty,
                      self.txt.get("1.0","end").strip()))
        conn.commit(); conn.close()
        if self.callback: self.callback()
        self.destroy()


# ─────────────────────────────────────────────────────────────────────────────
# USERS TAB (admin only)
# ─────────────────────────────────────────────────────────────────────────────
class UsersTab(ttk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user
        self._build()
        self.load()

    def _build(self):
        tb = tk.Frame(self, bg=BG)
        tb.pack(fill="x", padx=10, pady=(10,4))
        ttk.Button(tb,text="➕ Add User",command=self._add,
                   style="Success.TButton").pack(side="left",padx=(0,6))
        ttk.Button(tb,text="🗑 Delete",command=self._delete,
                   style="Danger.TButton").pack(side="left",padx=6)
        ttk.Button(tb,text="🔄",command=self.load).pack(side="right")

        cols   = ["#","Username","Role","Full Name","Created"]
        widths = [40, 120,      80,    200,         160]
        frame, self.tree = make_tree(self, cols, widths)
        frame.pack(fill="both", expand=True, padx=10, pady=4)

    def load(self):
        for r in self.tree.get_children(): self.tree.delete(r)
        for i, u in enumerate(db.get_all_users(), 1):
            self.tree.insert("","end", iid=str(u["id"]),
                             values=(i, u["username"], u["role"],
                                     u["full_name"], u.get("created_at","")))

    def _sel(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Select","Please select a user."); return None
        return int(sel[0])

    def _add(self): UserDialog(self, callback=self.load)

    def _delete(self):
        uid = self._sel()
        if uid is None: return
        if uid == self.user["id"]:
            messagebox.showerror("Error","You cannot delete your own account."); return
        if messagebox.askyesno("Confirm","Delete this user account?"):
            db.delete_user(uid); self.load()


class UserDialog(tk.Toplevel):
    def __init__(self, parent, callback=None):
        super().__init__(parent)
        self.title("Add New User")
        self.configure(bg=BG)
        self.resizable(False, False)
        self.grab_set()
        self.callback = callback
        self._build()
        self._center()

    def _center(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - self.winfo_width())  // 2
        y = (self.winfo_screenheight() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")

    def _build(self):
        f = tk.Frame(self,bg=BG,padx=24,pady=20); f.pack(fill="both",expand=True)
        tk.Label(f,text="New User Account",font=FONT_H,bg=BG,fg=ACCENT2).grid(
            row=0,column=0,columnspan=2,pady=(0,14),sticky="w")
        lbl(f,"Full Name *").grid(row=1,column=0,sticky="w",pady=3)
        self.v_name = tk.StringVar()
        entry(f,self.v_name,32).grid(row=1,column=1,sticky="ew",pady=3)
        lbl(f,"Username *").grid(row=2,column=0,sticky="w",pady=3)
        self.v_username = tk.StringVar()
        entry(f,self.v_username,32).grid(row=2,column=1,sticky="ew",pady=3)
        lbl(f,"Password *").grid(row=3,column=0,sticky="w",pady=3)
        self.v_password = tk.StringVar()
        e = entry(f,self.v_password,32); e.config(show="•")
        e.grid(row=3,column=1,sticky="ew",pady=3)
        lbl(f,"Role *").grid(row=4,column=0,sticky="w",pady=3)
        self.v_role = tk.StringVar(value="nurse")
        combo(f,["admin","nurse","surgeon"],self.v_role,30).grid(
            row=4,column=1,sticky="ew",pady=3)
        sep(f).grid(row=5,column=0,columnspan=2,sticky="ew",pady=12)
        bf = tk.Frame(f,bg=BG); bf.grid(row=6,column=0,columnspan=2,sticky="e")
        ttk.Button(bf,text="Cancel",command=self.destroy).pack(side="right",padx=(6,0))
        ttk.Button(bf,text="Create Account",command=self._save,
                   style="Success.TButton").pack(side="right")

    def _save(self):
        name     = self.v_name.get().strip()
        username = self.v_username.get().strip()
        password = self.v_password.get().strip()
        role     = self.v_role.get()
        if not name or not username or not password:
            messagebox.showerror("Validation","All fields are required.",parent=self); return
        conn   = db.get_connection()
        exists = conn.execute("SELECT id FROM users WHERE username=?",(username,)).fetchone()
        conn.close()
        if exists:
            messagebox.showerror("Error",f"Username '{username}' is already taken.",parent=self); return

        new_id = db.add_user({"username":username,"password":password,"role":role,"full_name":name})

        # If surgeon role, offer to link to an existing surgeon record
        if role == "surgeon":
            unlinked = db.get_unlinked_surgeons()
            if unlinked:
                surgeon_map = {s["name"]: s["id"] for s in unlinked}
                LinkSurgeonDialog(self, new_id, surgeon_map)   # modal – blocks until closed
            else:
                messagebox.showinfo(
                    "Note",
                    "No unlinked surgeon records found.\n"
                    "Go to the Surgeons tab, add a surgeon record, "
                    "then use 'Link User' to connect this account.",
                    parent=self
                )

        messagebox.showinfo("Success", f"Account '{username}' created!", parent=self)
        if self.callback: self.callback()
        self.destroy()


class LinkSurgeonDialog(tk.Toplevel):
    """Let admin link a newly-created surgeon user to a surgeon record."""
    def __init__(self, parent, user_id, surgeon_map):
        super().__init__(parent)
        self.title("Link Surgeon Account")
        self.configure(bg=BG)
        self.resizable(False, False)
        self.grab_set()
        self.user_id     = user_id
        self.surgeon_map = surgeon_map
        self._build()
        self._center()

    def _center(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - self.winfo_width())  // 2
        y = (self.winfo_screenheight() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")

    def _build(self):
        f = tk.Frame(self, bg=BG, padx=30, pady=24)
        f.pack(fill="both", expand=True)

        tk.Label(f, text="Link to Surgeon Record",
                 font=FONT_H, bg=BG, fg=ACCENT2).pack(pady=(0,10))
        tk.Label(f,
                 text="Choose which surgeon profile this login account belongs to.\n"
                      "This is required for the surgeon to see their assigned surgeries.",
                 bg=BG, fg=SUBTEXT, font=("Segoe UI",9), wraplength=300,
                 justify="left").pack(anchor="w", pady=(0,12))

        lbl(f, "Surgeon Record:").pack(anchor="w")
        self.v_surgeon = tk.StringVar()
        combo(f, list(self.surgeon_map.keys()), self.v_surgeon, 32).pack(fill="x", pady=(4,16))

        sep(f).pack(fill="x", pady=8)

        bf = tk.Frame(f, bg=BG)
        bf.pack(anchor="e")
        ttk.Button(bf, text="Skip", command=self.destroy).pack(side="right", padx=(6,0))
        ttk.Button(bf, text="Link", command=self._save,
                   style="Success.TButton").pack(side="right")

    def _save(self):
        name = self.v_surgeon.get()
        if not name or name not in self.surgeon_map:
            messagebox.showerror("Error", "Please select a surgeon record.", parent=self)
            return
        db.link_surgeon_to_user(self.surgeon_map[name], self.user_id)
        messagebox.showinfo("Linked",
                            f"Account linked to '{name}' — they can now see their surgeries.",
                            parent=self)
        self.destroy()


class LinkUserToSurgeonDialog(tk.Toplevel):
    """Admin picks a user account to link to an existing surgeon record."""
    def __init__(self, parent, surgeon_id, user_map, callback=None):
        super().__init__(parent)
        self.title("Link User to Surgeon")
        self.configure(bg=BG)
        self.resizable(False, False)
        self.grab_set()
        self.surgeon_id = surgeon_id
        self.user_map   = user_map
        self.callback   = callback
        self._build()
        self._center()

    def _center(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - self.winfo_width())  // 2
        y = (self.winfo_screenheight() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")

    def _build(self):
        f = tk.Frame(self, bg=BG, padx=30, pady=24)
        f.pack(fill="both", expand=True)

        tk.Label(f, text=f"Link User → Surgeon #{self.surgeon_id}",
                 font=FONT_H, bg=BG, fg=ACCENT2).pack(pady=(0,12))
        tk.Label(f,
                 text="Select the user account that belongs to this surgeon.\n"
                      "After linking, that user will see their surgeries when they log in.",
                 bg=BG, fg=SUBTEXT, font=("Segoe UI",9), wraplength=300,
                 justify="left").pack(anchor="w", pady=(0,12))

        lbl(f, "User Account:").pack(anchor="w")
        self.v_user = tk.StringVar()
        combo(f, list(self.user_map.keys()), self.v_user, 32).pack(fill="x", pady=(4,16))

        sep(f).pack(fill="x", pady=8)

        bf = tk.Frame(f, bg=BG)
        bf.pack(anchor="e")
        ttk.Button(bf, text="Cancel", command=self.destroy).pack(side="right", padx=(6,0))
        ttk.Button(bf, text="Link", command=self._save,
                   style="Success.TButton").pack(side="right")

    def _save(self):
        name = self.v_user.get()
        if not name or name not in self.user_map:
            messagebox.showerror("Error", "Please select a user.", parent=self)
            return
        db.link_surgeon_to_user(self.surgeon_id, self.user_map[name])
        messagebox.showinfo("Done",
                            f"Surgeon #{self.surgeon_id} linked to '{name}' successfully.",
                            parent=self)
        if self.callback: self.callback()
        self.destroy()


# ─────────────────────────────────────────────────────────────────────────────
# REPORTS TAB (admin only)
# ─────────────────────────────────────────────────────────────────────────────
class ReportsTab(ttk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user
        self._build()

    def _build(self):
        import matplotlib
        matplotlib.use("TkAgg")

        paned = ttk.PanedWindow(self, orient="horizontal")
        paned.pack(fill="both", expand=True, padx=10, pady=10)

        left = tk.Frame(paned, bg=PANEL, width=240)
        left.pack_propagate(False)
        paned.add(left, weight=0)

        tk.Label(left,text="📊 Reports",font=FONT_H,bg=PANEL,fg=ACCENT2).pack(pady=(18,10))
        tk.Label(left,text="GRAPHICAL CHARTS",font=("Segoe UI",8,"bold"),
                 bg=PANEL,fg=SUBTEXT).pack(anchor="w",padx=14,pady=(10,4))

        charts = [
            ("Surgeries by Status",   reports.chart_surgeries_by_status),
            ("Surgeries by Surgeon",  reports.chart_surgeries_by_surgeon),
            ("Monthly Volume",        reports.chart_surgeries_by_month),
            ("Priority Distribution", reports.chart_priority_distribution),
            ("Surgery Types",         reports.chart_surgery_types),
        ]

        right = tk.Frame(paned, bg=BG)
        paned.add(right, weight=1)

        def show_chart(fn):
            fig = fn()
            if fig is None: return
            for w in right.winfo_children(): w.destroy()
            import io
            from PIL import Image, ImageTk
            buf = io.BytesIO()
            fig.savefig(buf, format="png", dpi=100, bbox_inches="tight",
                        facecolor=fig.get_facecolor())
            buf.seek(0)
            img   = Image.open(buf)
            photo = ImageTk.PhotoImage(img)
            lw    = tk.Label(right, image=photo, bg=BG)
            lw.image = photo
            lw.pack(fill="both", expand=True)
            import matplotlib.pyplot as plt
            plt.close(fig)

        for name, fn in charts:
            ttk.Button(left, text=name, command=lambda f=fn: show_chart(f),
                       width=28).pack(padx=14, pady=3, fill="x")

        sep(left).pack(fill="x", padx=14, pady=14)
        tk.Label(left,text="LIST-BASED EXPORT",font=("Segoe UI",8,"bold"),
                 bg=PANEL,fg=SUBTEXT).pack(anchor="w",padx=14,pady=(0,4))

        def do_export(fn, label):
            try:
                path = fn()
                messagebox.showinfo("Exported", f"{label} saved to:\n{path}")
            except Exception as ex:
                messagebox.showerror("Error", str(ex))

        exports = [
            ("📄 Surgeries CSV",   reports.export_surgeries_csv,   "CSV"),
            ("📊 Surgeries Excel", reports.export_surgeries_excel, "Excel"),
            ("📊 Patients Excel",  reports.export_patients_excel,  "Excel"),
            ("📊 Surgeons Excel",  reports.export_surgeons_excel,  "Excel"),
        ]
        for name, fn, fmt in exports:
            ttk.Button(left, text=name,
                       command=lambda f=fn, l=fmt+f" {name}": do_export(f,l),
                       width=28).pack(padx=14, pady=3, fill="x")

        tk.Label(left, text="Files saved to:\n./reports/",
                 font=("Segoe UI",8), bg=PANEL, fg=SUBTEXT,
                 wraplength=210, justify="left").pack(padx=14, pady=(12,0))

        tk.Label(right, text="Select a chart from the left panel",
                 font=("Segoe UI",13), bg=BG, fg=SUBTEXT).pack(expand=True)


# ─────────────────────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    db.init_db()
    LoginWindow().mainloop()