import unittest

from generate import *


class TestGenerate(unittest.TestCase):
    def test_extract_title_basic(self):
        md = """
# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien
"""
        title = extract_title(md)
        self.assertEqual(title, "Tolkien Fan Club")

    def test_extract_title_exception(self):
        md = """
## Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien
"""

        with self.assertRaises(Exception):
            extract_title(md)
#        self.assertRaises(Exception, extract_title, md) - another way of the same testing

if __name__ == "__main__":
    unittest.main()
