import java.io.File;
import java.io.FileInputStream;
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
			String body = readTextFromFile("c:\\java_sources\\input\\hello.txt");

			createPdf(dir, path, body, font);

			System.out.println("Created : " + path);
			System.out.println("Body : " + body); 

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static String readTextFromFile(String dir){
		FileInputStream inputStream = null; // 파일 읽기 스트림
		String readData = "";
		
		try
		{
			inputStream = new FileInputStream(dir);// 파일 입력 스트림 생성

			byte[] readBuffer = new byte[1024];
			while (inputStream.read(readBuffer, 0, readBuffer.length) != -1);
			
			readData = new String(readBuffer);
		}
		catch (Exception e)
		{
			System.out.println("파일 입출력 에러!!" + e);
		}
		finally
		{
			try
			{
				inputStream.close();
			}
			catch (Exception e)
			{
				System.out.println("닫기 실패" + e);
			}
		}

		return readData;
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
