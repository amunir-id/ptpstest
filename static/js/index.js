import { create, registerPlugin } from "filepond";
import "filepond/dist/filepond.min.css";

// Import the Image Preview plugin
import FilePondPluginImagePreview from "filepond-plugin-image-preview";

// Register the plugin with FilePond
registerPlugin(FilePondPluginImagePreview);

// Get a file input reference
const input = document.querySelector('input[type="file"]');

// Create a FilePond instance
create(input);
