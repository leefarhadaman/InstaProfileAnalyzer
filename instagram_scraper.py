import os
import json
import instaloader

# Create an instance of Instaloader
loader = instaloader.Instaloader()

def fetch_instagram_details(username):
    try:
        # Create a folder for the username to store all fetched data
        directory = username
        os.makedirs(directory, exist_ok=True)

        # Fetch profile details
        print(f"Fetching details for profile: {username}...")
        profile = instaloader.Profile.from_username(loader.context, username)

        # Extract profile details
        details = {
            "Username": profile.username,
            "Full Name": profile.full_name,
            "Bio": profile.biography,
            "Profile URL": f"https://www.instagram.com/{profile.username}/",
            "External URL": profile.external_url,
            "Total Posts": profile.mediacount,
            "Followers": profile.followers,
            "Following": profile.followees,
        }

        # Save the profile picture
        print(f"Downloading profile picture...")
        profile_pic_path = os.path.join(directory, f"{username}_profile_pic.jpg")
        loader.download_profilepic(profile)
        for file in os.listdir(profile.username):
            if file.startswith("profile_pic"):
                os.rename(os.path.join(profile.username, file), profile_pic_path)
        details["Profile Picture"] = profile_pic_path

        # Initialize variables to calculate the total likes and comments
        total_likes = 0
        total_comments = 0
        highest_likes = 0
        highest_comments = 0
        highest_liked_post = None
        highest_commented_post = None

        print(f"Processing posts to find highest likes and comments...")
        for post in profile.get_posts():
            # Calculate total likes and comments
            total_likes += post.likes
            total_comments += post.comments

            # Find the highest liked and commented posts
            if post.likes > highest_likes:
                highest_likes = post.likes
                highest_liked_post = post

            if post.comments > highest_comments:
                highest_comments = post.comments
                highest_commented_post = post

        details["Total Likes"] = total_likes
        details["Total Comments"] = total_comments
        details["Highest Likes"] = highest_likes
        details["Highest Comments"] = highest_comments

        # Fetch the highest liked image
        if highest_liked_post:
            print(f"Downloading image with the highest likes...")
            highest_liked_image_path = os.path.join(directory, "highest_liked.jpg")
            loader.download_post(highest_liked_post, target=f"{directory}/highest_liked_post")
            for file in os.listdir(f"{directory}/highest_liked_post"):
                if file.endswith(".jpg"):
                    os.rename(
                        os.path.join(f"{directory}/highest_liked_post", file),
                        highest_liked_image_path
                    )
            details["Highest Liked Image"] = highest_liked_image_path

        # Fetch the highest commented image
        if highest_commented_post:
            print(f"Downloading image with the highest comments...")
            highest_commented_image_path = os.path.join(directory, "highest_commented.jpg")
            loader.download_post(highest_commented_post, target=f"{directory}/highest_commented_post")
            for file in os.listdir(f"{directory}/highest_commented_post"):
                if file.endswith(".jpg"):
                    os.rename(
                        os.path.join(f"{directory}/highest_commented_post", file),
                        highest_commented_image_path
                    )
            details["Highest Commented Image"] = highest_commented_image_path

        # Save the data to a JSON file
        json_file_path = os.path.join(directory, f"{username}_details.json")
        print(f"Saving data to JSON file...")
        with open(json_file_path, 'w') as json_file:
            json.dump(details, json_file, indent=4)

        print(f"Data saved successfully to {json_file_path}")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile '{username}' does not exist or is private!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    username = input("Enter the Instagram username: ")
    fetch_instagram_details(username)
