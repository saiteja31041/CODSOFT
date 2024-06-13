import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        self.contacts = []

        # Add contact section
        self.add_frame = tk.Frame(root)
        self.add_frame.pack(pady=10)

        self.name_label = tk.Label(self.add_frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.add_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(self.add_frame, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.add_frame)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = tk.Label(self.add_frame, text="Email:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.add_frame)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.address_label = tk.Label(self.add_frame, text="Address:")
        self.address_label.grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.add_frame)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.add_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        # View contacts section
        self.view_frame = tk.Frame(root)
        self.view_frame.pack(pady=10)

        self.contacts_listbox = tk.Listbox(self.view_frame, width=50, height=10)
        self.contacts_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.view_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.contacts_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.contacts_listbox.yview)

        # Search and update section
        self.search_frame = tk.Frame(root)
        self.search_frame.pack(pady=10)

        self.search_label = tk.Label(self.search_frame, text="Search by Name or Phone:")
        self.search_label.grid(row=0, column=0, padx=5, pady=5)
        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_contact)
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        self.update_button = tk.Button(self.search_frame, text="Update Selected", command=self.update_contact)
        self.update_button.grid(row=0, column=3, padx=5, pady=5)

        self.delete_button = tk.Button(self.search_frame, text="Delete Selected", command=self.delete_contact)
        self.delete_button.grid(row=0, column=4, padx=5, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone:
            contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
            self.contacts.append(contact)
            self.update_contacts_listbox()
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and phone are required.")

    def update_contacts_listbox(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def search_contact(self):
        search_term = self.search_entry.get().lower()
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            if search_term in contact['name'].lower() or search_term in contact['phone']:
                self.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def update_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.contacts[index]['name'] = self.name_entry.get()
            self.contacts[index]['phone'] = self.phone_entry.get()
            self.contacts[index]['email'] = self.email_entry.get()
            self.contacts[index]['address'] = self.address_entry.get()
            self.update_contacts_listbox()
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please select a contact to update.")

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.contacts[index]
            self.update_contacts_listbox()
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

root = tk.Tk()
app = ContactManager(root)
root.mainloop()
