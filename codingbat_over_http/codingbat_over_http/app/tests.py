from urllib import response
from django.test import SimpleTestCase

# Create your tests here.
class TestStringSplosion(SimpleTestCase):
    def test_splosion_ab(self):
        response = self.client.get("/warmup-2/string-splosion/ab")
        self.assertContains(response, 'aab')

    def test_splosion_abc(self):
        response = self.client.get("/warmup-2/string-splosion/abc")
        self.assertContains(response, 'aababc')

    def test_splosion_Code(self):
        response = self.client.get("/warmup-2/string-splosion/Code")
        self.assertContains(response, 'CCoCodCode')

class TestCatDog(SimpleTestCase):
    def test_catdog(self):
        response = self.client.get("/string-2/cat-dog/catdog")
        self.assertContains(response, True)

    def test_catdog_sum(self):
        response = self.client.get("/string-2/cat-dog/1cat1cadodog")
        self.assertContains(response, True)

    def test_catdog_cat(self):
        response = self.client.get("/string-2/cat-dog/catcat")
        self.assertContains(response, False)

class TestNearHundred(SimpleTestCase):
    def test_near_hundred_93(self):
        response = self.client.get("/warmup-1/near-hundred/93")
        self.assertContains(response, True)

    def test_near_hundred_90(self):
        response = self.client.get("/warmup-1/near-hundred/90")
        self.assertContains(response, True)
    
    def test_near_hundred_89(self):
        response = self.client.get("/warmup-1/near-hundred/89")
        self.assertContains(response, False)

class TestLoneSum(SimpleTestCase):
    def test_lone_sum_6(self):
        response = self.client.get("/logic-2/lone-sum/1/2/3")
        self.assertContains(response, 6)

    def test_lone_sum_2(self):
        response = self.client.get("/logic-2/lone-sum/3/2/3")
        self.assertContains(response, 2)

    def test_lone_sum_0(self):
        response = self.client.get("/logic-2/lone-sum/3/3/3")
        self.assertContains(response, 0)