// Pontificia Universidad Javeriana Cali
// Multimedia
// Dilan Chávez

String media_path = "../../../media/";
String out_path = "/out/";

void setup()
{
  PImage plazaImg = loadImage(media_path + "plaza.png");
  PImage lenaImg = loadImage(media_path + "lena.jpg");
  
  size(378, 568);
  
  image(plazaImg, 0, 0);
  for(int i = 0; i < lenaImg.pixels.length; i++) {
  	float r = red(lenaImg.pixels[i]);
  	float g = green(lenaImg.pixels[i]);
  	float b = blue(lenaImg.pixels[i]);
  	lenaImg.pixels[i] = color(r, g, b, 128);
  }
  image(lenaImg, 0, 0);
  
  saveFrame(out_path + "punto1_out.jpg");
}
