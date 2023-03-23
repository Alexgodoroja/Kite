from django.test import TestCase
from django.core.exceptions import ValueError
from blogs.models import Post, Comments, user
from datetime import datetime

class CommentsModelTestCase(TestCase):

    fixtures = [
        "blogs/tests/fixtures/default_user.json",
        "blogs/tests/fixtures/default_club.json",
    ]
    
    def setUp(self):
        self.user = User.objects.get(username='@johnsmith')
        
        self.post = Post.objects.create(
            author=self.user,
            text='This is a test post.'
        )
        
        self.comment = Comments.objects.create(
            post=self.post,
            author=self.user,
            text='This is a test comment.'
        )

    def test_comment_is_created_correctly(self):
        """Test that a Comment is created correctly"""
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.author, self.user)
        self.assertEqual(self.comment.text, 'This is a test comment.')
        self.assertTrue(isinstance(self.comment.created_at, datetime))

    def test_comment_is_deleted_when_post_is_deleted(self):
        """Test that a Comment is deleted when its associated Post is deleted"""
        post_id = self.post.id
        self.post.delete()
        self.assertFalse(Comments.objects.filter(post_id=post_id).exists())

    def test_comment_is_deleted_when_user_is_deleted(self):
        """Test that a Comment is deleted when its associated User is deleted"""
        user_id = self.user.id
        self.user.delete()
        self.assertFalse(Comments.objects.filter(author_id=user_id).exists())

    def test_comment_can_be_280_length(self):
        """Test that the Comment text field has a max length of 280"""
        max_length = Comments._meta.get_field('text').max_length
        self.assertEqual(max_length, 280)

    def test_comment_cannot_be_blank(self):
        """Test that the Comment text field cannot be blank"""
        with self.assertRaises(ValueError):
            comment = Comments.objects.create(post=self.post, author=self.user, text='')

    def test_comment_cannot_be_null(self):
        """Test that the Comment text field cannot be null"""
        with self.assertRaises(ValueError):
            comment = Comments.objects.create(post=self.post, author=self.user, text=None)

    def test_comment_post_cannot_be_null(self):
        """Test that the Comment post field cannot be null"""
        with self.assertRaises(ValueError):
            comment = Comments.objects.create(post=None, author=self.user, text='Test Comment')

    def test_comment_author_cannot_be_null(self):
        """Test that the Comment author field cannot be null"""
        with self.assertRaises(ValueError):
            comment = Comments.objects.create(post=self.post, author=None, text='Test Comment')

    def test_comments_are_ordered_chronologically(self):
        """Test that Comments are ordered by the creation date"""
        comment1 = Comments.objects.create(post=self.post, author=self.user, text='Comment 1')
        comment2 = Comments.objects.create(post=self.post, author=self.user, text='Comment 2')
        comment3 = Comments.objects.create(post=self.post, author=self.user, text='Comment 3')
        self.assertEqual(list(self.post.comments.all()), [comment3, comment2, comment1, self.comment])
