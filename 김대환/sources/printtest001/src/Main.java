import java.io.File;
import java.io.FileOutputStream;

import com.itextpdf.text.Document;
import com.itextpdf.text.Paragraph;
import com.itextpdf.text.pdf.PdfWriter;

public class Main {

	public static void main(String[] args) {
		try {
			String fileName = "test.pdf";
			String dir = "c:\\java_sources\\output";
			String path = dir + "\\" + fileName;

			String body = "Hello World.";

			createPdf(path, body);

			System.out.println("Created : " + path);
			System.out.println("Body : " + body);

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static void createPdf(String path, String text) throws Exception {
		File directory = new File(path);
		
		if (!directory.exists())
			directory.mkdirs();

		Document document = new Document();
		PdfWriter.getInstance(document, new FileOutputStream(path));

		document.open();
		document.add(new Paragraph(text));
		document.close();
	}
}
