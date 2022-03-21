try:
        import unittest
        import requests
except Exception as e:
        print("Some modules are missing{}".format(e))

class FlaskTest(unittest.TestCase):
        URL="https://zip-county-api.herokuapp.com/create_phase"
        data={"name": "KARTIKEY DWIVEDI", "zip": "02215"}
        #check for the response 200
        def test_status(self):
            resp=requests.post(self.URL,json=self.data)
            self.assertEqual(resp.status_code,200)
            print("POST method called")
        #check if county is correct
        def test_county(self):
            resp=requests.post(self.URL,json=self.data)
            self.assertEqual(resp.json()["county"],"Suffolk County")
            print("County is correct")
        #check if pig latin name is correct
        def test_pig_latin_name(self):
            resp=requests.post(self.URL,json=self.data)
            self.assertEqual(resp.json()["pig_latin_name"],"Artikeykay ivedidway")
            print("Pig latin name is correct")
        #check if population is correct
        def test_population(self):
            resp=requests.post(self.URL,json=self.data)
            self.assertEqual(resp.json()["population"],24698)
            print("Population is correct")
        #check if zip is correct
        def test_zipcode(self):
            resp=requests.post(self.URL,json=self.data)
            self.assertEqual(resp.json()["zip"],"02215")
            print("Zipcode is correct")


if __name__ == "__main__":
    tester=FlaskTest()
    tester.test_status()
    tester.test_county()
    tester.test_pig_latin_name()
    tester.test_population()
    tester.test_zipcode()