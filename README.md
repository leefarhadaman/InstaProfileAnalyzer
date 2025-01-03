# InstaProfileAnalyzer - Version 1.0

🚀 **Analyze Public Instagram Profiles with Ease**

InstaProfileAnalyzer is a Python-based tool designed to fetch and analyze data from **public Instagram profiles**. This is the **first version** of the tool, offering key insights into profile details, post analytics, and more.

## Key Features

- **Fetch Profile Details**: Bio, username, external links, and profile picture.
- **Analyze Posts**:
  - Total number of posts.
  - Posts with the highest likes and comments.
  - Total likes and comments across all posts.
- **Organized Output**:
  - Store data in JSON format.
  - Download profile pictures and top post images into organized folders.

## Tech Stack

- **Python**: For scripting and automation.
- **Instaloader Library**: For retrieving Instagram data.
- **JSON**: For structured data storage.
- **OS Module**: For file and directory management.

## How It Works

1. Enter the Instagram username of the public profile.
2. The tool fetches profile details and analyzes post data.
3. Data is stored:
   - In a JSON file.
   - Images in a directory named after the username.

## Future Plans

- Support for private profiles (within your network).
- Deeper post and engagement analytics.
- Enhanced performance and user experience.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/leefarhadaman/InstaProfileAnalyzer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd InstaProfileAnalyzer
   ```
3. Install the required dependencies:
   ```bash
   pip install instaloader
   ```
4. Run the script:
   ```bash
   python instaprofileanalyzer.py
   ```

## Usage

- Ensure you have Python installed on your system.
- Run the script and follow the prompts to enter a public Instagram username.
- The fetched data and images will be stored in a folder named after the username.

## Contributions

Contributions are welcome! Feel free to fork this repository and submit pull requests with improvements or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

⭐ **Star this repository if you found it helpful!**
