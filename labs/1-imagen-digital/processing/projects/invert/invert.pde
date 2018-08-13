String media_path = "../../media/";
String out_path = "../../out/";

void setup(){
  PImage img = loadImage(media_path + "lena.jpg");
  size(512, 512);
  img.loadPixels();
  for (int y=0; y<img.height; y++) {
    for (int x=0; x<img.width; x++) {
      color c = img.get(x,y);
      img.set(x, y, color(255 - red(c), 255 - green(c), 255 - blue(c)));
    }
  }
  image(img,0,0);
  saveFrame(out_path + "lena-inv.jpg");
}
