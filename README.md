<body>

<h1>Background Remover Program</h1>

<p>This Python program allows users to remove the background from images in various formats. Users can select images from their PC, process them to remove the background, and save the output as either a transparent PNG or a white-background JPG. The program uses <code>rembg</code> for background removal and <code>Pillow</code> for image processing, along with <code>Tkinter</code> for a user-friendly file selection interface.</p>

<h2>Features</h2>
<ul>
    <li>Supports multiple input image formats: <code>.png</code>, <code>.jpg</code>, <code>.jpeg</code>, <code>.gif</code>, <code>.tiff</code>, <code>.svg</code>, <code>.webp</code>, and <code>.bmp</code></li>
    <li>Allows the user to select an image file from their computer</li>
    <li>Saves the output image as either PNG (with transparency) or JPG (with a white background)</li>
    <li>Uses a file dialog for easy selection of input and output files</li>
</ul>

<h2>Requirements</h2>
<p>Make sure you have the following libraries installed:</p>
<ul>
    <li><code>rembg</code></li>
    <li><code>Pillow</code></li>
    <li><code>Tkinter</code> (built-in with Python for most platforms)</li>
</ul>

<p>You can install the necessary libraries by running:</p>
<pre><code>pip install rembg pillow</code></pre>

<h2>How to Use</h2>
<ol>
    <li><strong>Run the Program:</strong> Start the program by running:<br>
    <pre><code>python background_remover.py</code></pre></li>
    <li><strong>Select Input Image:</strong> A file dialog will appear to select an input image file from your computer. Make sure to select a file with a supported format.</li>
    <li><strong>Select Save Location:</strong> After selecting the input image, another file dialog will appear for you to choose the output location and filename.</li>
    <li><strong>Output Image:</strong> The program saves the image as a transparent PNG by default. If you choose a <code>.jpg</code> extension for the output file, it will save the image with a white background instead.</li>
</ol>

<h2>Program Structure</h2>
<ul>
    <li><code>select_file()</code>: Opens a dialog for selecting the input image file.</li>
    <li><code>select_save_location()</code>: Opens a dialog for choosing where to save the output image.</li>
    <li><code>remove_background()</code>: Processes the image to remove the background and save it in the chosen format.</li>
    <li><strong>Main:</strong> The main function orchestrates the file selection and calls the background removal function.</li>
</ul>

<h2>Supported Formats</h2>
<ul>
    <li><strong>Input:</strong> PNG, JPG, JPEG, GIF, TIFF, SVG, WEBP, BMP</li>
    <li><strong>Output:</strong> PNG (for transparent background), JPG (with a white background)</li>
</ul>

<h2>Example Usage</h2>
<pre><code>python background_remover.py</code></pre>
<p>Follow the on-screen prompts to select the input image and the location for the output image.</p>

<h2>Example</h2>
<ul>
    <li><strong>Input:</strong> <code>example_image.jpg</code></li>
    <li><strong>Output:</strong> <code>output_image.png</code> (with a transparent background) or <code>output_image.jpg</code> (with a white background)</li>
</ul>

<h2>Notes</h2>
<ul>
    <li>PNG output will preserve transparency where the background was removed.</li>
    <li>JPG output will replace transparency with a white background.</li>
</ul>

<h2>License</h2>
<p>This project is open-source and freely available for use and modification.</p>

</body>
