PImage img;

String media_path = "../../media/";
String out_path = "../../out/";

int frame = 80;
int current_frame = 0;

void setup() {
  
  img = loadImage(media_path + "lena.jpg");
  size(512, 512);
  image(img, 0, 0);
} 

void draw() {
  if(current_frame == frame){
    saveFrame(out_path + "lena-out-" + frame + ".jpg");
  }
  for (int y = 1; y < img.height-1; y++) {
    for (int x = 1; x < img.width-1; x++) {
      int newX = randInt(x-1, x+1);
      int newY = randInt(y-1, y+1);
      set(x, y, get(newX, newY));
    }
  }
  current_frame++;
} 


int randInt(int low, int high) {
  int r = floor(random(low, high+1));
  r = constrain(r, low, high);
  return r;
}
