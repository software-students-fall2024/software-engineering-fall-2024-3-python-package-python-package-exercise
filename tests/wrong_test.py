import unittest
from src.ascii_art_TNH.ascii_art import wrong_input

class TestMyCode(unittest.TestCase):
  def test_wrong_input_multi(self):
      result = wrong_input("frog frog",2)
      flowers = r"""
              ,,,                      ,,,
        {{{}}    ,,,             {{{}}    ,,,
      ,,, ~Y~    {{{}},,,      ,,, ~Y~    {{{}},,,
    {{}}} |/,,,  ~Y~{{}}}    {{}}} |/,,,  ~Y~{{}}}
      ~Y~ \|{{}}}/\|/ ~Y~  ,,, ~Y~ \|{{}}}/\|/ ~Y~  ,,,
      \|/ \|/~Y~  \|,,,|/ {{}}}\|/ \|/~Y~  \|,,,|/ {{}}}
      \|/ \|/\|/  \{{{}}/  ~Y~ \|/ \|/\|/  \{{{}}/  ~Y~
      \|/\\|/\|/ \\|~Y~//  \|/ \|/\\|/\|/ \\|~Y~//  \|/
      \|//\|/\|/,\\|/|/|// \|/ \|//\|/\|/,\\|/|/|// \|/
  jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  """
      self.assertEqual(result.strip(),flowers.strip())