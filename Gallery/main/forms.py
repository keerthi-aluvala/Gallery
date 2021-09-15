from django import forms

from main.models import post


class CreateBlogPostForm(forms.ModelForm):

	class Meta:
		model = post
		fields = ['ImgName', 'ImgURL', 'ImgDetails']


class UpdateBlogPostForm(forms.ModelForm):

	class Meta:
		model = post
		fields = ['ImgName', 'ImgURL', 'ImgDetails']

	def save(self, commit=True):
		blog_post = self.instance
		blog_post.ImgName = self.cleaned_data['ImgName']
		blog_post.ImgURL = self.cleaned_data['ImgURL']
		blog_post.ImgDetails = self.cleaned_data['ImgDetails']

		if commit:
			blog_post.save()
		return blog_post