import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import PyPDF2
import os
from PIL import Image  # Used for saving extracted images in common formats
import io


class PDFMaster:
    """
    A class to perform various PDF manipulation tasks using PyPDF2.
    Methods are adapted to report status via a callback.
    """

    def __init__(self, status_callback=None):
        self.status_callback = status_callback if status_callback else print

    def _update_status(self, message):
        """Sends a message to the GUI's status area."""
        self.status_callback(message)

    def _get_pdf_reader_writer(self, input_path):
        """Helper to get PdfReader and PdfWriter objects."""
        try:
            reader = PyPDF2.PdfReader(input_path)
            writer = PyPDF2.PdfWriter()
            return reader, writer
        except PyPDF2.errors.PdfReadError:
            self._update_status(
                f"Error: Could not read PDF file at {input_path}. It might be encrypted or corrupted.")
            return None, None
        except FileNotFoundError:
            self._update_status(f"Error: File not found at {input_path}.")
            return None, None
        except Exception as e:
            self._update_status(
                f"An unexpected error occurred while opening {input_path}: {e}")
            return None, None

    def merge_pdfs(self, input_paths, output_path):
        """Merges multiple PDF files into a single PDF."""
        pdf_merger = PyPDF2.PdfMerger()
        self._update_status(f"Attempting to merge {len(input_paths)} PDFs...")
        try:
            for path in input_paths:
                if not os.path.exists(path):
                    self._update_status(
                        f"Warning: Input file not found: {path}. Skipping.")
                    continue
                pdf_merger.append(path)

            with open(output_path, 'wb') as output_file:
                pdf_merger.write(output_file)
            self._update_status(f"PDFs merged successfully to: {output_path}")
        except Exception as e:
            self._update_status(f"Error merging PDFs: {e}")
        finally:
            pdf_merger.close()

    def split_pdf(self, input_path, output_folder):
        """Splits a PDF file into individual pages, saving each as a new PDF."""
        reader, _ = self._get_pdf_reader_writer(input_path)
        if not reader:
            return

        os.makedirs(output_folder, exist_ok=True)
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        num_pages = len(reader.pages)
        self._update_status(
            f"Splitting '{input_path}' into {num_pages} pages...")

        try:
            for i in range(num_pages):
                writer = PyPDF2.PdfWriter()
                writer.add_page(reader.pages[i])
                output_filename = os.path.join(
                    output_folder, f"{base_name}_page_{i + 1}.pdf")
                with open(output_filename, 'wb') as output_pdf:
                    writer.write(output_pdf)
                self._update_status(f"  Saved: {output_filename}")
            self._update_status(
                f"PDF split successfully into {num_pages} files in: {output_folder}")
        except Exception as e:
            self._update_status(f"Error splitting PDF: {e}")

    def rotate_pages(self, input_path, output_path, pages_to_rotate, rotation_angle):
        """Rotates specified pages in a PDF file."""
        if rotation_angle not in [90, 180, 270]:
            self._update_status(
                "Error: Rotation angle must be 90, 180, or 270 degrees.")
            return

        reader, writer = self._get_pdf_reader_writer(input_path)
        if not reader:
            return

        num_pages = len(reader.pages)
        self._update_status(f"Rotating pages in '{input_path}'...")

        try:
            for i in range(num_pages):
                page = reader.pages[i]
                if not pages_to_rotate or (i + 1) in pages_to_rotate:
                    page.rotate(rotation_angle)
                    self._update_status(
                        f"  Page {i + 1} rotated by {rotation_angle} degrees.")
                writer.add_page(page)

            with open(output_path, 'wb') as output_pdf:
                writer.write(output_pdf)
            self._update_status(
                f"Pages rotated successfully to: {output_path}")
        except Exception as e:
            self._update_status(f"Error rotating pages: {e}")

    def extract_pages(self, input_path, output_path, page_numbers):
        """Extracts specific pages from a PDF file into a new PDF."""
        reader, writer = self._get_pdf_reader_writer(input_path)
        if not reader:
            return

        num_pages = len(reader.pages)
        self._update_status(
            f"Extracting pages {page_numbers} from '{input_path}'...")

        try:
            for page_num in page_numbers:
                if 1 <= page_num <= num_pages:
                    writer.add_page(reader.pages[page_num - 1])
                    self._update_status(f"  Added page {page_num}.")
                else:
                    self._update_status(
                        f"Warning: Page {page_num} is out of range (1-{num_pages}). Skipping.")

            if len(writer.pages) > 0:
                with open(output_path, 'wb') as output_pdf:
                    writer.write(output_pdf)
                self._update_status(
                    f"Pages extracted successfully to: {output_path}")
            else:
                self._update_status(
                    "No pages were extracted. Output PDF not created.")
        except Exception as e:
            self._update_status(f"Error extracting pages: {e}")

    def add_page_from_pdf(self, main_pdf_path, page_to_add_path, output_path, insert_at_page_num):
        """Adds a page from another PDF into the main PDF at a specified position."""
        main_reader, main_writer = self._get_pdf_reader_writer(main_pdf_path)
        if not main_reader:
            return

        add_reader, _ = self._get_pdf_reader_writer(page_to_add_path)
        if not add_reader:
            return
        if not add_reader.pages:
            self._update_status(
                f"Error: No pages found in {page_to_add_path}.")
            return

        page_to_insert = add_reader.pages[0]

        num_main_pages = len(main_reader.pages)
        self._update_status(
            f"Adding page from '{page_to_add_path}' to '{main_pdf_path}' at position {insert_at_page_num}...")

        try:
            for i in range(num_main_pages):
                if i == insert_at_page_num - 1:
                    main_writer.add_page(page_to_insert)
                    self._update_status(
                        f"  Inserted new page at position {insert_at_page_num}.")
                main_writer.add_page(main_reader.pages[i])

            if insert_at_page_num > num_main_pages:
                main_writer.add_page(page_to_insert)
                self._update_status(
                    f"  Inserted new page at the end (position {num_main_pages + 1}).")

            with open(output_path, 'wb') as output_pdf:
                main_writer.write(output_pdf)
            self._update_status(f"Page added successfully to: {output_path}")
        except Exception as e:
            self._update_status(f"Error adding page: {e}")

    def replace_page(self, main_pdf_path, page_to_replace_with_path, output_path, page_number_to_replace):
        """Replaces a specific page in the main PDF with a page from another PDF."""
        main_reader, main_writer = self._get_pdf_reader_writer(main_pdf_path)
        if not main_reader:
            return

        replace_reader, _ = self._get_pdf_reader_writer(
            page_to_replace_with_path)
        if not replace_reader:
            return
        if not replace_reader.pages:
            self._update_status(
                f"Error: No pages found in {page_to_replace_with_path}.")
            return

        replacement_page = replace_reader.pages[0]

        num_main_pages = len(main_reader.pages)
        if not (1 <= page_number_to_replace <= num_main_pages):
            self._update_status(
                f"Error: Page number {page_number_to_replace} is out of range (1-{num_main_pages}).")
            return

        self._update_status(
            f"Replacing page {page_number_to_replace} in '{main_pdf_path}' with page from '{page_to_replace_with_path}'...")

        try:
            for i in range(num_main_pages):
                if (i + 1) == page_number_to_replace:
                    main_writer.add_page(replacement_page)
                    self._update_status(
                        f"  Replaced page {page_number_to_replace}.")
                else:
                    main_writer.add_page(main_reader.pages[i])

            with open(output_path, 'wb') as output_pdf:
                main_writer.write(output_pdf)
            self._update_status(
                f"Page replaced successfully to: {output_path}")
        except Exception as e:
            self._update_status(f"Error replacing page: {e}")

    def extract_images(self, input_path, output_folder):
        """Extracts images from a PDF file."""
        reader, _ = self._get_pdf_reader_writer(input_path)
        if not reader:
            return

        os.makedirs(output_folder, exist_ok=True)
        image_count = 0
        self._update_status(f"Extracting images from '{input_path}'...")

        try:
            for page_num, page in enumerate(reader.pages):
                for image_idx, image in enumerate(page.images):
                    try:
                        pil_image = Image.open(io.BytesIO(image.data))
                        output_filename = os.path.join(
                            output_folder, f"page_{page_num + 1}_img_{image_idx + 1}.{pil_image.format.lower()}")
                        pil_image.save(output_filename)
                        image_count += 1
                        self._update_status(f"  Extracted: {output_filename}")
                    except Exception as img_e:
                        self._update_status(
                            f"  Warning: Could not extract image {image_idx + 1} from page {page_num + 1}. Error: {img_e}")
                        output_filename = os.path.join(
                            output_folder, f"page_{page_num + 1}_img_{image_idx + 1}.raw")
                        with open(output_filename, 'wb') as f:
                            f.write(image.data)
                        self._update_status(
                            f"  Saved raw image data to: {output_filename}")

            if image_count > 0:
                self._update_status(
                    f"Successfully extracted {image_count} images to: {output_folder}")
            else:
                self._update_status(
                    "No images found or extracted from the PDF.")
        except Exception as e:
            self._update_status(f"Error extracting images: {e}")

    def remove_pages(self, input_path, output_path, pages_to_remove):
        """Removes specified pages from a PDF file."""
        reader, writer = self._get_pdf_reader_writer(input_path)
        if not reader:
            return

        num_pages = len(reader.pages)
        pages_removed_count = 0
        self._update_status(
            f"Removing pages {pages_to_remove} from '{input_path}'...")

        try:
            for i in range(num_pages):
                if (i + 1) not in pages_to_remove:
                    writer.add_page(reader.pages[i])
                else:
                    pages_removed_count += 1
                    self._update_status(f"  Removed page {i + 1}.")

            if pages_removed_count > 0:
                with open(output_path, 'wb') as output_pdf:
                    writer.write(output_pdf)
                self._update_status(
                    f"Pages removed successfully to: {output_path}")
            else:
                self._update_status(
                    "No pages were removed. Output PDF not created.")
        except Exception as e:
            self._update_status(f"Error removing pages: {e}")


class PDFMasterGUI:
    def __init__(self, master):
        self.master = master
        master.title("PDF Master")
        # Slightly increased height for better spacing
        master.geometry("800x650")
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        # --- Styling ---
        self.style = ttk.Style()
        self.style.theme_use('clam')  # A good base theme for customization

        # Define colors
        self.colors = {
            "primary_bg": "#2C3E50",    # Dark Slate Blue
            "secondary_bg": "#34495E",  # Lighter Slate Blue for frames
            "accent_blue": "#3498DB",   # Bright Blue
            "accent_green": "#2ECC71",  # Emerald Green
            "text_light": "#ECF0F1",    # Light Grey
            "text_dark": "#2C3E50",     # Dark text for light elements
            "entry_bg": "#ECF0F1",      # Light background for entries
            "status_bg": "#22313F"      # Even darker for status bar
        }

        # Configure general styles
        # Changed font from 'Inter' to 'Arial' for better cross-platform compatibility
        self.style.configure(
            '.', background=self.colors["primary_bg"], foreground=self.colors["text_light"], font=('Arial', 10))
        self.style.configure('TFrame', background=self.colors["secondary_bg"])
        self.style.configure(
            'TLabel', background=self.colors["secondary_bg"], foreground=self.colors["text_light"])
        self.style.configure('TButton',
                             background=self.colors["accent_blue"],
                             foreground=self.colors["text_light"],
                             font=('Arial', 10, 'bold'),  # Changed font here
                             padding=6,
                             relief="flat")
        self.style.map('TButton',
                       background=[('active', self.colors["accent_green"]),
                                   ('!disabled', self.colors["accent_blue"])],
                       foreground=[('active', self.colors["text_light"])])

        self.style.configure(
            'TEntry', fieldbackground=self.colors["entry_bg"], foreground=self.colors["text_dark"], borderwidth=1, relief="flat")
        self.style.configure(
            'TListbox', background=self.colors["entry_bg"], foreground=self.colors["text_dark"], borderwidth=1, relief="flat")
        self.style.configure('TCombobox', fieldbackground=self.colors["entry_bg"], foreground=self.colors["text_dark"],
                             selectbackground=self.colors["accent_blue"], selectforeground=self.colors["text_light"])
        self.style.configure(
            'TRadiobutton', background=self.colors["secondary_bg"], foreground=self.colors["text_light"])
        # Prevent background change on hover
        self.style.map('TRadiobutton', background=[
                       ('active', self.colors["secondary_bg"])])

        # Notebook (Tab) styling
        self.style.configure(
            'TNotebook', background=self.colors["primary_bg"], borderwidth=0)
        self.style.configure('TNotebook.Tab',
                             background=self.colors["secondary_bg"],
                             foreground=self.colors["text_light"],
                             padding=[10, 5],
                             font=('Arial', 10, 'bold'))  # Changed font here
        self.style.map('TNotebook.Tab',
                       background=[('selected', self.colors["accent_blue"])],
                       foreground=[('selected', self.colors["text_light"])])

        self.pdf_master = PDFMaster(self.update_status)

        self.notebook = ttk.Notebook(master, style='TNotebook')
        self.notebook.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.create_merge_tab()
        self.create_split_tab()
        self.create_extract_pages_tab()
        self.create_remove_pages_tab()
        self.create_rotate_pages_tab()
        self.create_add_replace_page_tab()
        self.create_extract_images_tab()

        # Status Bar
        self.status_frame = ttk.LabelFrame(
            master, text="Status / Log", style='TFrame')
        self.status_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        self.status_frame.grid_columnconfigure(0, weight=1)

        self.status_text = tk.Text(self.status_frame, height=8, wrap="word", state="disabled",
                                   bg=self.colors["status_bg"], fg=self.colors["text_light"],
                                   # Changed font here
                                   font=('Arial', 9), relief="flat", borderwidth=0)
        self.status_text.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.status_text_scrollbar = ttk.Scrollbar(
            self.status_frame, command=self.status_text.yview)
        self.status_text_scrollbar.grid(row=0, column=1, sticky="ns")
        self.status_text.config(yscrollcommand=self.status_text_scrollbar.set)

        self.update_status(
            "Welcome to PDF Master! Select an operation from the tabs above.")

    def update_status(self, message):
        """Updates the status text area in the GUI."""
        self.status_text.config(state="normal")
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.see(tk.END)  # Auto-scroll to the end
        self.status_text.config(state="disabled")
        self.master.update_idletasks()  # Force update GUI

    def clear_status(self):
        """Clears the status text area."""
        self.status_text.config(state="normal")
        self.status_text.delete(1.0, tk.END)
        self.status_text.config(state="disabled")

    def _create_common_widgets(self, parent_frame, input_label_text="Input PDF:", output_label_text="Output PDF:",
                               show_pages_input=False, show_angle_input=False, show_source_page_input=False,
                               input_is_multiple=False, output_is_folder=False):
        """Helper to create common input/output widgets for tabs."""
        widgets = {}
        row_idx = 0

        # Input PDF(s)
        input_frame = ttk.Frame(parent_frame, style='TFrame')
        input_frame.grid(row=row_idx, column=0, columnspan=2,
                         sticky="ew", pady=5, padx=5)
        input_frame.grid_columnconfigure(1, weight=1)
        ttk.Label(input_frame, text=input_label_text, style='TLabel').grid(
            row=0, column=0, padx=5, sticky="w")

        if input_is_multiple:
            widgets['input_listbox'] = tk.Listbox(input_frame, height=4, width=50,
                                                  bg=self.colors["entry_bg"], fg=self.colors["text_dark"],
                                                  selectbackground=self.colors[
                                                      "accent_blue"], selectforeground=self.colors["text_light"],
                                                  relief="flat", borderwidth=1)
            widgets['input_listbox'].grid(
                row=1, column=0, columnspan=2, padx=5, sticky="ew")
            widgets['input_files'] = []  # Store actual paths

            add_button = ttk.Button(input_frame, text="Add PDF(s)", command=lambda: self._add_input_files(
                widgets['input_listbox'], widgets['input_files']))
            add_button.grid(row=2, column=0, padx=5, pady=2, sticky="w")

            clear_button = ttk.Button(input_frame, text="Clear List", command=lambda: self._clear_input_files(
                widgets['input_listbox'], widgets['input_files']))
            clear_button.grid(row=2, column=1, padx=5, pady=2, sticky="e")
            row_idx += 3  # Adjust row index for listbox
        else:
            widgets['input_entry'] = ttk.Entry(
                input_frame, width=60, style='TEntry')
            widgets['input_entry'].grid(row=0, column=1, padx=5, sticky="ew")
            ttk.Button(input_frame, text="Browse...", command=lambda: self._browse_file(
                widgets['input_entry'], "open")).grid(row=0, column=2, padx=5)
            row_idx += 1

        # Source Page PDF (for add/replace)
        if show_source_page_input:
            source_frame = ttk.Frame(parent_frame, style='TFrame')
            source_frame.grid(row=row_idx, column=0,
                              columnspan=2, sticky="ew", pady=5, padx=5)
            source_frame.grid_columnconfigure(1, weight=1)
            ttk.Label(source_frame, text="Source Page PDF:", style='TLabel').grid(
                row=0, column=0, padx=5, sticky="w")
            widgets['source_page_entry'] = ttk.Entry(
                source_frame, width=60, style='TEntry')
            widgets['source_page_entry'].grid(
                row=0, column=1, padx=5, sticky="ew")
            ttk.Button(source_frame, text="Browse...", command=lambda: self._browse_file(
                widgets['source_page_entry'], "open")).grid(row=0, column=2, padx=5)
            row_idx += 1

        # Pages Input
        if show_pages_input:
            pages_frame = ttk.Frame(parent_frame, style='TFrame')
            pages_frame.grid(row=row_idx, column=0,
                             columnspan=2, sticky="ew", pady=5, padx=5)
            pages_frame.grid_columnconfigure(1, weight=1)
            ttk.Label(pages_frame, text="Page Numbers (e.g., 1,3,5-7):",
                      style='TLabel').grid(row=0, column=0, padx=5, sticky="w")
            widgets['pages_entry'] = ttk.Entry(
                pages_frame, width=60, style='TEntry')
            widgets['pages_entry'].grid(row=0, column=1, padx=5, sticky="ew")
            row_idx += 1

        # Rotation Angle Input
        if show_angle_input:
            angle_frame = ttk.Frame(parent_frame, style='TFrame')
            angle_frame.grid(row=row_idx, column=0,
                             columnspan=2, sticky="ew", pady=5, padx=5)
            angle_frame.grid_columnconfigure(1, weight=1)
            ttk.Label(angle_frame, text="Rotation Angle:", style='TLabel').grid(
                row=0, column=0, padx=5, sticky="w")
            widgets['angle_var'] = tk.StringVar(value="90")  # Default value
            angle_options = [90, 180, 270]
            widgets['angle_menu'] = ttk.OptionMenu(
                angle_frame, widgets['angle_var'], *angle_options, style='TCombobox')
            widgets['angle_menu'].grid(row=0, column=1, padx=5, sticky="ew")
            row_idx += 1

        # Output PDF/Folder
        output_frame = ttk.Frame(parent_frame, style='TFrame')
        output_frame.grid(row=row_idx, column=0, columnspan=2,
                          sticky="ew", pady=5, padx=5)
        output_frame.grid_columnconfigure(1, weight=1)
        ttk.Label(output_frame, text=output_label_text, style='TLabel').grid(
            row=0, column=0, padx=5, sticky="w")
        widgets['output_entry'] = ttk.Entry(
            output_frame, width=60, style='TEntry')
        widgets['output_entry'].grid(row=0, column=1, padx=5, sticky="ew")

        if output_is_folder:
            ttk.Button(output_frame, text="Browse Folder...", command=lambda: self._browse_file(
                widgets['output_entry'], "folder")).grid(row=0, column=2, padx=5)
        else:
            ttk.Button(output_frame, text="Save As...", command=lambda: self._browse_file(
                widgets['output_entry'], "save")).grid(row=0, column=2, padx=5)
        row_idx += 1

        return widgets, row_idx

    def _browse_file(self, entry_widget, dialog_type):
        """Opens a file dialog and sets the selected path to the entry widget."""
        if dialog_type == "open":
            filepath = filedialog.askopenfilename(
                filetypes=[("PDF files", "*.pdf")])
        elif dialog_type == "save":
            filepath = filedialog.asksaveasfilename(
                defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        elif dialog_type == "folder":
            filepath = filedialog.askdirectory()
        else:
            filepath = None

        if filepath:
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, filepath)

    def _add_input_files(self, listbox_widget, file_list_storage):
        """Adds selected PDF files to the listbox for merging."""
        filepaths = filedialog.askopenfilenames(
            filetypes=[("PDF files", "*.pdf")])
        if filepaths:
            for fp in filepaths:
                listbox_widget.insert(tk.END, os.path.basename(fp))
                file_list_storage.append(fp)

    def _clear_input_files(self, listbox_widget, file_list_storage):
        """Clears the listbox and the stored file paths for merging."""
        listbox_widget.delete(0, tk.END)
        file_list_storage.clear()

    def _parse_pages(self, pages_str):
        """Parses a comma-separated string of page numbers/ranges into a list of integers."""
        if not pages_str:
            return []
        page_list = []
        try:
            parts = pages_str.split(',')
            for part in parts:
                part = part.strip()
                if '-' in part:
                    start, end = map(int, part.split('-'))
                    if start > end:
                        raise ValueError(
                            "Start page cannot be greater than end page in a range.")
                    page_list.extend(range(start, end + 1))
                else:
                    page_list.append(int(part))
            return sorted(list(set(page_list)))  # Remove duplicates and sort
        except ValueError as e:
            messagebox.showerror(
                "Input Error", f"Invalid page number format: {e}. Please use formats like '1,3,5' or '2-5'.")
            return None

    # --- Tab Creation Methods ---
    def create_merge_tab(self):
        tab = ttk.Frame(self.notebook, padding="10", style='TFrame')
        self.notebook.add(tab, text="Merge PDFs")
        tab.grid_columnconfigure(0, weight=1)

        widgets, row_idx = self._create_common_widgets(tab, input_label_text="PDFs to Merge:",
                                                       output_label_text="Merged Output PDF:",
                                                       input_is_multiple=True, output_is_folder=False)

        merge_button = ttk.Button(
            tab, text="Merge PDFs", command=lambda: self._execute_merge(widgets))
        merge_button.grid(row=row_idx, column=0, pady=10)

    def _execute_merge(self, widgets):
        self.clear_status()
        input_paths = widgets['input_files']
        output_path = widgets['output_entry'].get()

        if not input_paths:
            self.update_status("Error: Please add PDF files to merge.")
            return
        if not output_path:
            self.update_status(
                "Error: Please specify an output file for the merged PDF.")
            return

        self.pdf_master.merge_pdfs(input_paths, output_path)

    def create_split_tab(self):
        tab = ttk.Frame(self.notebook, padding="10", style='TFrame')
        self.notebook.add(tab, text="Split PDF")
        tab.grid_columnconfigure(0, weight=1)

        widgets, row_idx = self._create_common_widgets(tab, input_label_text="Input PDF to Split:",
                                                       output_label_text="Output Folder for Pages:",
                                                       input_is_multiple=False, output_is_folder=True)

        split_button = ttk.Button(
            tab, text="Split PDF", command=lambda: self._execute_split(widgets))
        split_button.grid(row=row_idx, column=0, pady=10)

    def _execute_split(self, widgets):
        self.clear_status()
        input_path = widgets['input_entry'].get()
        output_folder = widgets['output_entry'].get()

        if not input_path:
            self.update_status("Error: Please select an input PDF to split.")
            return
        if not output_folder:
            self.update_status(
                "Error: Please select an output folder for split pages.")
            return

        self.pdf_master.split_pdf(input_path, output_folder)

    def create_extract_pages_tab(self):
        tab = ttk.Frame(self.notebook, padding="10", style='TFrame')
        self.notebook.add(tab, text="Extract Pages")
        tab.grid_columnconfigure(0, weight=1)

        widgets, row_idx = self._create_common_widgets(tab, input_label_text="Input PDF:",
                                                       output_label_text="Output PDF for Extracted Pages:",
                                                       show_pages_input=True)

        extract_button = ttk.Button(
            tab, text="Extract Pages", command=lambda: self._execute_extract_pages(widgets))
        extract_button.grid(row=row_idx, column=0, pady=10)

    def _execute_extract_pages(self, widgets):
        self.clear_status()
        input_path = widgets['input_entry'].get()
        output_path = widgets['output_entry'].get()
        pages_str = widgets['pages_entry'].get()
        pages_to_extract = self._parse_pages(pages_str)

        if not input_path:
            self.update_status("Error: Please select an input PDF.")
            return
        if not output_path:
            self.update_status("Error: Please specify an output file.")
            return
        if pages_to_extract is None:  # Error during parsing
            return
        if not pages_to_extract:
            self.update_status("Error: Please enter page numbers to extract.")
            return

        self.pdf_master.extract_pages(
            input_path, output_path, pages_to_extract)

    def create_remove_pages_tab(self):
        tab = ttk.Frame(self.notebook, padding="10", style='TFrame')
        self.notebook.add(tab, text="Remove Pages")
        tab.grid_columnconfigure(0, weight=1)

        widgets, row_idx = self._create_common_widgets(tab, input_label_text="Input PDF:",
                                                       output_label_text="Output PDF (Pages Removed):",
                                                       show_pages_input=True)

        remove_button = ttk.Button(
            tab, text="Remove Pages", command=lambda: self._execute_remove_pages(widgets))
        remove_button.grid(row=row_idx, column=0, pady=10)

    def _execute_remove_pages(self, widgets):
        self.clear_status()
        input_path = widgets['input_entry'].get()
        output_path = widgets['output_entry'].get()
        pages_str = widgets['pages_entry'].get()
        pages_to_remove = self._parse_pages(pages_str)

        if not input_path:
            self.update_status("Error: Please select an input PDF.")
            return
        if not output_path:
            self.update_status("Error: Please specify an output file.")
            return
        if pages_to_remove is None:  # Error during parsing
            return
        if not pages_to_remove:
            self.update_status("Error: Please enter page numbers to remove.")
            return

        self.pdf_master.remove_pages(input_path, output_path, pages_to_remove)

    def create_rotate_pages_tab(self):
        tab = ttk.Frame(self.notebook, padding="10", style='TFrame')
        self.notebook.add(tab, text="Rotate Pages")
        tab.grid_columnconfigure(0, weight=1)

        widgets, row_idx = self._create_common_widgets(tab, input_label_text="Input PDF:",
                                                       output_label_text="Output PDF (Pages Rotated):",
                                                       show_pages_input=True, show_angle_input=True)

        rotate_button = ttk.Button(
            tab, text="Rotate Pages", command=lambda: self._execute_rotate_pages(widgets))
        rotate_button.grid(row=row_idx, column=0, pady=10)

    def _execute_rotate_pages(self, widgets):
        self.clear_status()
        input_path = widgets['input_entry'].get()
        output_path = widgets['output_entry'].get()
        pages_str = widgets['pages_entry'].get()
        pages_to_rotate = self._parse_pages(pages_str)
        rotation_angle = int(widgets['angle_var'].get())

        if not input_path:
            self.update_status("Error: Please select an input PDF.")
            return
        if not output_path:
            self.update_status("Error: Please specify an output file.")
            return
        if pages_to_rotate is None:  # Error during parsing
            return
        # pages_to_rotate can be empty if all pages are to be rotated, so no check here.

        self.pdf_master.rotate_pages(
            input_path, output_path, pages_to_rotate, rotation_angle)

    def create_add_replace_page_tab(self):
        tab = ttk.Frame(self.notebook, padding="10", style='TFrame')
        self.notebook.add(tab, text="Add/Replace Page")
        tab.grid_columnconfigure(0, weight=1)

        widgets, row_idx = self._create_common_widgets(tab, input_label_text="Main PDF:",
                                                       output_label_text="Output PDF:",
                                                       show_source_page_input=True)

        # Action choice (Add or Replace)
        action_frame = ttk.Frame(tab, style='TFrame')
        action_frame.grid(row=row_idx, column=0, columnspan=2,
                          sticky="ew", pady=5, padx=5)
        ttk.Label(action_frame, text="Action:", style='TLabel').grid(
            row=0, column=0, padx=5, sticky="w")
        widgets['action_var'] = tk.StringVar(value="add")  # Default to add
        ttk.Radiobutton(action_frame, text="Add Page", variable=widgets['action_var'], value="add", style='TRadiobutton').grid(
            row=0, column=1, padx=5, sticky="w")
        ttk.Radiobutton(action_frame, text="Replace Page", variable=widgets['action_var'], value="replace", style='TRadiobutton').grid(
            row=0, column=2, padx=5, sticky="w")
        row_idx += 1

        # Target Page Number
        target_page_frame = ttk.Frame(tab, style='TFrame')
        target_page_frame.grid(row=row_idx, column=0,
                               columnspan=2, sticky="ew", pady=5, padx=5)
        target_page_frame.grid_columnconfigure(1, weight=1)
        ttk.Label(target_page_frame, text="Target Page Number (1-based):",
                  style='TLabel').grid(row=0, column=0, padx=5, sticky="w")
        widgets['target_page_entry'] = ttk.Entry(
            target_page_frame, width=10, style='TEntry')
        widgets['target_page_entry'].grid(row=0, column=1, padx=5, sticky="w")
        row_idx += 1

        perform_button = ttk.Button(
            tab, text="Perform Action", command=lambda: self._execute_add_replace_page(widgets))
        perform_button.grid(row=row_idx, column=0, pady=10)

    def _execute_add_replace_page(self, widgets):
        self.clear_status()
        main_pdf_path = widgets['input_entry'].get()
        source_page_path = widgets['source_page_entry'].get()
        output_path = widgets['output_entry'].get()
        action_type = widgets['action_var'].get()

        try:
            target_page_num = int(widgets['target_page_entry'].get())
        except ValueError:
            self.update_status("Error: Target Page Number must be an integer.")
            return

        if not main_pdf_path or not source_page_path or not output_path:
            self.update_status(
                "Error: Please fill all required fields (Main PDF, Source Page PDF, Output PDF).")
            return

        if action_type == "add":
            self.pdf_master.add_page_from_pdf(
                main_pdf_path, source_page_path, output_path, target_page_num)
        elif action_type == "replace":
            self.pdf_master.replace_page(
                main_pdf_path, source_page_path, output_path, target_page_num)

    def create_extract_images_tab(self):
        tab = ttk.Frame(self.notebook, padding="10", style='TFrame')
        self.notebook.add(tab, text="Extract Images")
        tab.grid_columnconfigure(0, weight=1)

        widgets, row_idx = self._create_common_widgets(tab, input_label_text="Input PDF:",
                                                       output_label_text="Output Folder for Images:",
                                                       input_is_multiple=False, output_is_folder=True)

        extract_button = ttk.Button(
            tab, text="Extract Images", command=lambda: self._execute_extract_images(widgets))
        extract_button.grid(row=row_idx, column=0, pady=10)

    def _execute_extract_images(self, widgets):
        self.clear_status()
        input_path = widgets['input_entry'].get()
        output_folder = widgets['output_entry'].get()

        if not input_path:
            self.update_status("Error: Please select an input PDF.")
            return
        if not output_folder:
            self.update_status(
                "Error: Please select an output folder for images.")
            return

        self.pdf_master.extract_images(input_path, output_folder)


def main():
    root = tk.Tk()
    app = PDFMasterGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
