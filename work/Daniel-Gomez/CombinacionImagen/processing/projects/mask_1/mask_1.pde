
String media_path = "../../media/";
String out_path = "../../out/";

void setup() {
  PImage img = loadImage(media_path + "lena.jpg");
  PImage msk = loadImage(media_path + "mask.jpg");
  
  background(0);
  size(512, 512);
  //img.mask(msk);
  image(img, 0, 0);
  tint(255, 127);
  image(msk, 0, 0);
  saveFrame(out_path + "lena-mask-1.jpg");
}
