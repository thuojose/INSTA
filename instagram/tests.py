from django.test import TestCase
from .models import Profile
from django.shortcuts import get_object_or_404

class ProfileTestClass(TestCase):
    #set-up method
    def setUp(self):
        self.prof=Profile(id=1,bio='Engineer')
        self.prof.save_profile()
        self.prof.update_profile()
        self.prof.update_profile()
        
    #testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.prof,Profile))
    
    #testing the save_method
    def test_save_method(self):
        self.prof.save_profile()
        prof = Profile.objects.all()
        self.assertTrue(len(prof) > 0)
        
    #testing the image update_method
    def test_update_profile_method(self):
        prof=Profile.objects.filter(id=1).update_profile(bio='Programmer')
        self.prof.save()
    
    #testing updated image instance
    def test_instance(self):
        self.assertTrue(isinstance(self.prof,Profile))
        

  #set-up method for testing the delete method
    def setUp(self):
        self.prof = Profile(id=1,bio='Engineer')
        self.prof.save()
        
        
    #testing the delete_method
    def test_delete_method(self):
        # img = get_object_or_404(Image,pk=1)
        prof=Profile.objects.filter(id=1).delete()
        self.assertTrue(len(prof) > 0)
    
    #tear-down the instance
    def tearDown(self):
        Profile.objects.all().delete()

