import tempfile
import unittest
from pathlib import Path
import cv2
import numpy as np
from image import imageSearch, hasImageReturnCoor


class TemplateMatchingTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        rng = np.random.default_rng(17)
        self.template = rng.integers(1, 255, (8, 9, 3), dtype=np.uint8)
        self.image = rng.integers(1, 255, (35, 40, 3), dtype=np.uint8)
        self.image[12:20, 16:25] = self.template
        self.image_path = self.root / 'image.png'
        self.template_path = self.root / 'template.png'
        cv2.imwrite(str(self.image_path), self.image)
        cv2.imwrite(str(self.template_path), self.template)

    def test_both_methods_return_the_correct_match_position(self):
        expected = {'x': 31, 'y': 52}
        self.assertEqual(imageSearch(self.image_path, self.template_path), expected)
        self.assertEqual(hasImageReturnCoor(self.image_path, self.template_path), expected)

    def test_nonmatching_template_returns_false(self):
        rng = np.random.default_rng(42)
        cv2.imwrite(str(self.template_path), rng.integers(1, 255, (8, 9, 3), dtype=np.uint8))
        self.assertFalse(hasImageReturnCoor(self.image_path, self.template_path))

    def test_invalid_paths_and_oversized_templates_have_clear_errors(self):
        for args in [(None, self.template_path), (self.root / 'missing.png', self.template_path)]:
            with self.assertRaises(ValueError): imageSearch(*args)
        with self.assertRaises(ValueError): imageSearch(self.template_path, self.image_path)
        for threshold in [-0.1, 1.1, float('nan')]:
            with self.assertRaises(ValueError): hasImageReturnCoor(self.image_path, self.template_path, threshold)
