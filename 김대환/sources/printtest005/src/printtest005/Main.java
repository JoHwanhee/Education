package printtest005;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;

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
			
			String body = httpGet("http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastGrib",
					"yJtjzVRlbJncrau3ZGu10ywN0SRALcl4RBmz%2F7QuHzniFj%2FN4P2cPw9QFEfGWhwTiKXzVYR2w%2BkAU2dFhbEw4A%3D%3D",
					"20190114",
					"0600",
					"60",
					"127");
			

			createPdf(dir, path, body, font);

			System.out.println("Created : " + path);
			System.out.println("Body : " + body);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static String httpGet(String input_url, String serviceKey, String baseDate, 
			String baseTime, String nx, String ny) {
		
		StringBuilder sb = new StringBuilder();
		try {

			StringBuilder urlBuilder = new StringBuilder(input_url); 
			urlBuilder.append("?" + 
							  URLEncoder.encode("ServiceKey", "UTF-8") + 
							  "=" + serviceKey);
			
			urlBuilder.append("&" + 
					  URLEncoder.encode("base_date", "UTF-8") + 
					  "=" + baseDate);
			
			urlBuilder.append("&" + 
					  URLEncoder.encode("base_time", "UTF-8") + 
					  "=" + baseTime);
			
			urlBuilder.append("&" + 
					  URLEncoder.encode("nx", "UTF-8") + 
					  "=" + nx);
			
			urlBuilder.append("&" + 
					  URLEncoder.encode("ny", "UTF-8") + 
					  "=" + ny);
			
			urlBuilder.append("&" + 
					  URLEncoder.encode("_type", "UTF-8") + 
					  "=" + "json");
			
			System.out.println(urlBuilder.toString());
			
			URL url = new URL(urlBuilder.toString());
			HttpURLConnection conn = (HttpURLConnection) url.openConnection();
			conn.setRequestMethod("GET");
			conn.setRequestProperty("Content-type", "application/json");
			System.out.println("Response code: " + conn.getResponseCode());
			BufferedReader rd;
			if (conn.getResponseCode() >= 200 && conn.getResponseCode() <= 300) {
				rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
			} else {
				rd = new BufferedReader(new InputStreamReader(conn.getErrorStream()));
			}
			
			String line;
			while ((line = rd.readLine()) != null) {
				sb.append(line);
			}
			rd.close();
			conn.disconnect();
			

		} catch (Exception e) {
			// TODO: handle exception
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
