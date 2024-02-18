import unittest
from unittest.mock import Mock, patch
from looqbox.render.pdf.base_pdf_render import BasePDFRender, _get_rgb_color


class TestBasePDFRender(unittest.TestCase):

    # Testando a função _get_rgb_color

    def test_get_rgb_color_hex(self):
        self.assertEqual(_get_rgb_color("#ffffff"), (255, 255, 255))

    def test_get_rgb_color_rgb(self):
        self.assertEqual(_get_rgb_color("rgb(255, 255, 255)"), (255, 255, 255))

    def test_get_rgb_color_name(self):
        self.assertEqual(_get_rgb_color("red"), (255, 0, 0))

    def test_get_rgb_color_tuple(self):
        self.assertEqual(_get_rgb_color((255, 255, 255)), (255, 255, 255))

    # Testes para a classe BasePDFRender

    @patch("looqbox.render.pdf.pdf_builder.PDFBuilder")
    @patch("looqbox.render.pdf.base_pdf_render.GlobalCalling")
    def test_basepdfrender_init(self, mock_global_calling, mock_pdf_builder):
        mock_global_calling.looq.feature_flags = {"looqbot": {"linkOnAnswer": True, "watermark": True}}
        mock_global_calling.looq.domains[0].get.return_value = "domain"
        mock_global_calling.looq.question = "question"

        renderer = BasePDFRender()

        self.assertTrue(renderer.add_question_link)
        self.assertTrue(renderer.add_watermark)
        mock_pdf_builder.assert_called_once()

    @patch("looqbox.render.pdf.pdf_builder.PDFBuilder")
    @patch("looqbox.render.pdf.base_pdf_render.GlobalCalling")
    def test_basepdfrender_get_feature_flags(self, mock_global_calling, mock_pdf_builder):
        mock_global_calling.looq.feature_flags = {"looqbot": {"linkOnAnswer": True, "watermark": True}}

        renderer = BasePDFRender()
        add_question_link, add_watermark = renderer.get_feature_flags()

        self.assertTrue(add_question_link)
        self.assertTrue(add_watermark)

    @patch("looqbox.render.pdf.pdf_builder.PDFBuilder")
    @patch("looqbox.render.pdf.base_pdf_render.GlobalCalling")
    def test_basepdfrender_should_render(self, mock_global_calling, mock_pdf_builder):
        renderer = BasePDFRender()

        renderer.rendered_objs = ["ObjMessage"]
        self.assertFalse(renderer.should_render())

        renderer.rendered_objs = ["ObjMessage", "ObjPlotly"]
        self.assertTrue(renderer.should_render())


if __name__ == '__main__':
    unittest.main()
