import os
from PIL import Image
import argparse
import tkinter as tk  # Changed import: import tkinter as tk
# Removed Tk from here, now accessed via tk.Tk
from tkinter import filedialog, messagebox, ttk


class ImageToPDFConverter:
    """
    A class to convert image files (JPG, PNG, etc.) into a single PDF document.
    """

    def __init__(self):
        pass

    def convert_images_to_pdf(self, image_paths, output_pdf_path):
        """
        Converts a list of image files into a single PDF document.

        Args:
            image_paths (list): A list of paths to the image files.
            output_pdf_path (str): The path for the output PDF file.
        """
        if not image_paths:
            print("Error: No image files provided for conversion.")
            return

        images = []
        try:
            # Open the first image to determine mode and size for subsequent images
            first_image = Image.open(image_paths[0]).convert('RGB')
            images.append(first_image)

            for i, path in enumerate(image_paths[1:]):
                if not os.path.exists(path):
                    print(f"Warning: Image file not found: {path}. Skipping.")
                    continue

                # Open subsequent images and convert to RGB mode
                img = Image.open(path).convert('RGB')
                images.append(img)
                print(f"  Added image: {os.path.basename(path)}")

            # Save all opened images as a single PDF
            first_image.save(output_pdf_path, save_all=True,
                             append_images=images[1:])
            print(
                f"Successfully converted {len(images)} image(s) to PDF: {output_pdf_path}")

        except FileNotFoundError:
            print(f"Error: One or more image files not found.")
        except Exception as e:
            print(f"An error occurred during image to PDF conversion: {e}")

# --- Command Line Interface (CLI) ---


def main_cli():
    parser = argparse.ArgumentParser(
        description="Convert one or more image files to a single PDF.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("-i", "--input", nargs='+', required=True,
                        help="Input image file(s) (e.g., image1.jpg image2.png).")
    parser.add_argument("-o", "--output", required=True,
                        help="Output PDF file path (e.g., output.pdf).")

    args = parser.parse_args()
    converter = ImageToPDFConverter()
    converter.convert_images_to_pdf(args.input, args.output)

# --- GUI Interface ---


class ImageToPDFGUI:
    def __init__(self, master):
        self.master = master
        master.title("Image to PDF Converter")
        master.geometry("500x350")
        master.resizable(False, False)

        # Styling
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.colors = {
            "primary_bg": "#2C3E50",
            "secondary_bg": "#34495E",
            "accent_blue": "#3498DB",
            "accent_green": "#2ECC71",
            "text_light": "#ECF0F1",
            "text_dark": "#2C3E50",
            "entry_bg": "#ECF0F1",
            "status_bg": "#22313F"
        }
        self.style.configure(
            '.', background=self.colors["primary_bg"], foreground=self.colors["text_light"], font=('Arial', 10))
        self.style.configure('TFrame', background=self.colors["secondary_bg"])
        self.style.configure(
            'TLabel', background=self.colors["secondary_bg"], foreground=self.colors["text_light"])
        self.style.configure('TButton',
                             background=self.colors["accent_blue"],
                             foreground=self.colors["text_light"],
                             font=('Arial', 10, 'bold'),
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

        # Main Frame
        main_frame = ttk.Frame(master, padding="15", style='TFrame')
        main_frame.pack(fill="both", expand=True)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # Input Images
        input_frame = ttk.LabelFrame(
            main_frame, text="Input Images", style='TFrame')
        input_frame.grid(row=0, column=0, columnspan=2,
                         sticky="ew", pady=10, padx=5)
        input_frame.grid_columnconfigure(0, weight=1)

        self.image_listbox = tk.Listbox(input_frame, height=5, bg=self.colors["entry_bg"], fg=self.colors["text_dark"],
                                        selectbackground=self.colors["accent_blue"], selectforeground=self.colors["text_light"],
                                        relief="flat", borderwidth=1)
        self.image_listbox.pack(fill="both", expand=True, padx=5, pady=5)
        self.image_paths = []  # Store actual paths

        button_frame = ttk.Frame(input_frame, style='TFrame')
        button_frame.pack(fill="x", pady=5, padx=5)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)

        ttk.Button(button_frame, text="Add Image(s)", command=self._add_images).grid(
            row=0, column=0, padx=5, sticky="ew")
        ttk.Button(button_frame, text="Clear List", command=self._clear_images).grid(
            row=0, column=1, padx=5, sticky="ew")

        # Output PDF
        output_frame = ttk.LabelFrame(
            main_frame, text="Output PDF", style='TFrame')
        output_frame.grid(row=1, column=0, columnspan=2,
                          sticky="ew", pady=10, padx=5)
        output_frame.grid_columnconfigure(0, weight=1)

        self.output_entry = ttk.Entry(output_frame, width=50, style='TEntry')
        self.output_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        ttk.Button(output_frame, text="Save As...", command=self._browse_save_path).grid(
            row=0, column=1, padx=5, pady=5)

        # Convert Button
        ttk.Button(main_frame, text="Convert Images to PDF", command=self._execute_conversion).grid(
            row=2, column=0, columnspan=2, pady=15)

        # Status Bar
        self.status_label = ttk.Label(main_frame, text="Ready.", anchor="w", style='TLabel',
                                      background=self.colors["status_bg"], foreground=self.colors["text_light"])
        self.status_label.grid(
            row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.converter = ImageToPDFConverter()

    def _update_status(self, message):
        self.status_label.config(text=message)
        self.master.update_idletasks()

    def _add_images(self):
        filepaths = filedialog.askopenfilenames(
            filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
        if filepaths:
            for fp in filepaths:
                self.image_listbox.insert(tk.END, os.path.basename(fp))
                self.image_paths.append(fp)
            self._update_status(f"Added {len(filepaths)} image(s).")

    def _clear_images(self):
        self.image_listbox.delete(0, tk.END)
        self.image_paths.clear()
        self._update_status("Image list cleared.")

    def _browse_save_path(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if filepath:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, filepath)

    def _execute_conversion(self):
        self._update_status("Starting conversion...")
        output_pdf_path = self.output_entry.get()

        if not self.image_paths:
            messagebox.showerror(
                "Error", "Please add at least one image file.")
            self._update_status("Conversion failed: No images selected.")
            return
        if not output_pdf_path:
            messagebox.showerror(
                "Error", "Please specify an output PDF file path.")
            self._update_status("Conversion failed: No output path.")
            return

        # Pass the GUI's status update method to the converter
        self.converter.status_callback = self._update_status
        self.converter.convert_images_to_pdf(self.image_paths, output_pdf_path)

        # Reset status callback to default print after operation
        self.converter.status_callback = print


def main_gui():
    root = tk.Tk()
    app = ImageToPDFGUI(root)
    root.mainloop()


if __name__ == "__main__":
    # You can choose to run either the CLI or GUI version here
    # For a standalone GUI app, uncomment main_gui() and comment out main_cli()
    main_gui()
    # main_cli() # Uncomment this line and comment main_gui() to run the CLI version
