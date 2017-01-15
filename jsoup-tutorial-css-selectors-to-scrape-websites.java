import java.io.IOException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class Tutorial {	
	public static void main(String[] args) throws IOException  {
		Document doc = Jsoup.connect("http://techcrunch.com/2014/02/18/wattpad-offline-access-inline-commenting/").get();
		Elements li = doc.select("li.crunchbase-card *");
		Elements strong = li.select("strong.key, strong.key+span.value");
		Map <String, String> kv = new HashMap<String, String>();
		Iterator<Element> iter=strong.iterator();
		while (iter.hasNext()){
			Element key=(Element)iter.next();
			Element value =(Element)iter.next();
			kv.put(key.text(),value.text());
		}
		System.out.println(kv);
	}

}

/*
HTTP request without jsoup

URL url = new URL("http://www.techcrunch.com/");
URLConnection con = url.openConnection();
InputStream in = con.getInputStream();
String encoding = con.getContentEncoding();
encoding = encoding == null ? "UTF-8" : encoding;
ByteArrayOutputStream baos = new ByteArrayOutputStream();
byte[] buf = new byte[8192];
int len = 0;
while ((len = in.read(buf)) != -1) {
    baos.write(buf, 0, len);
}
String body = new String(baos.toByteArray(), encoding);
System.out.println(body);
*/
