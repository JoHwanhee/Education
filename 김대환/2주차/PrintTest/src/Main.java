import java.io.File;
import java.io.FileOutputStream;

import com.itextpdf.text.Document;
import com.itextpdf.text.Font;
import com.itextpdf.text.Paragraph;
import com.itextpdf.text.pdf.BaseFont;
import com.itextpdf.text.pdf.PdfWriter;

public class Main {

	public static void main(String[] args) {
		try {
			String fileName = "test.pdf";
			String dir = "c:\\java_sources\\output";
			String path = dir + "\\" + fileName;

			BaseFont bf = BaseFont.createFont("H2GTRM_0.TTF", "Identity-H", true);
			Font font  = new Font(bf, 13, Font.NORMAL);
			String body = "안녕하세요.";

			createPdf(dir, path, body, font);

			System.out.println("Created : " + path);
			System.out.println("Body : " + body); 

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static void createPdf(String dir, String full, String text, Font font) throws Exception {
		File directory = new File(dir);
		
		if (!directory.exists())
			directory.mkdirs();

		Document document = new Document();
		PdfWriter.getInstance(document, new FileOutputStream(full));

		Paragraph paragraph = new Paragraph(text, font);
		paragraph.setAlignment(0);
		
		document.open();
		document.add(paragraph);
		document.close();
	}
}
