package printtest003;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

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

			BaseFont bf = BaseFont.createFont("fonts\\H2GTRM.TTF", "Identity-H", true);
			Font font = new Font(bf, 13, Font.NORMAL);
			String body = httpGet("http://ahhoinn.dothome.co.kr/myData/hello.txt");

			createPdf(dir, path, body, font);

			System.out.println("Created : " + path);
			System.out.println("Body : " + body);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public static String httpGet(String input_url) {
		URL url;
		StringBuilder sb = new StringBuilder();
		
		try {
			url = new URL(input_url);
			HttpURLConnection conn = (HttpURLConnection) url.openConnection();
			conn.setRequestMethod("GET");
			conn.setRequestProperty("Content-type", "application/json");
			BufferedReader rd;
			if (conn.getResponseCode() >= 200 && conn.getResponseCode() <= 300) {
				rd = new BufferedReader(new InputStreamReader(conn.getInputStream(), "UTF-8"));
			} else {
				rd = new BufferedReader(new InputStreamReader(conn.getErrorStream(), "UTF-8"));
			}
			
			String data = rd.readLine();
			sb.append(data);
			
			rd.close();
			conn.disconnect();
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		return sb.toString();

	}


	private static void createPdf(String dir, String path, String text, Font font) {
		try {
			File directory = new File(dir);

			if (!directory.exists())
				directory.mkdirs();

			Document document = new Document();
			PdfWriter.getInstance(document, new FileOutputStream(path));

			document.open();
			Paragraph paragraph = new Paragraph(text, font);
			paragraph.setAlignment(0);

			document.add(paragraph);

			document.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
}
