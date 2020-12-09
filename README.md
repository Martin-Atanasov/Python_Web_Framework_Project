# Python_Web_Framework_Project
 Final Project of the course

BabyBook is a place where you can save and share your precious baby memories.
BabyBook makes it easy to keep track of all the fun stories and memories you share in your baby's first year, plus you can share it with the fam!
Are you sentimental and want to remember your child’s early years? Do you want to preserve these precious memories for when they’re older? You’re on the right place!
Share with your little one what the world was like when they were born. All those precious moments are backed up and kept private for you to share with those you choose.

Babybook is created on Django/Python/, it uses PostgreSQL as database.
You can create user, sign in, sign out.
Upon registration you have default profile picture/anonymous/ which you can change it later.
You can reset your password, by receiving an email with a private link.

You can register your kids, update their info and picture and delete their registration.
You can create stories with some information fields and a picture. You can chose the story to witch of your kids is related. You can update and delete the stories.
You can choose the status of the story, Private/it is available only to you/, Shared/it is available only to the registered users/ and Public/ it is available to all visitors of the web site in the Sneak Peek part.

When changing your profile picture the old one is removed from the server.
When changing the profile picture of a kid the old one is removed from the server.
When changing the picture of a story the old one is removed from the server.
When deleting a story its data and picture are deleted from the server.
When deleting a kid its data and picture are deleted from the server as well all related stories with its data an pictures.

If you want to create a Story and you don’t have a registered kid the asks you first to register at least one.
Only registered users can register kids and create stories.
