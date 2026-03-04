import cv2
import math
import os

class TemplateMatch:
    def __init__(self):
        pass

    def image_resolution_map(self, ratio_code):
        # ratio codes
        resolution_map = {
            "8r5": (800, 500),
            "43r18": (3440, 1440)
        }

        if ratio_code in resolution_map:
            print(f"template ratio {ratio_code} found in the resolution map")
            return resolution_map[ratio_code]
        else:
            print(f"template ratio {ratio_code} not found in the resolution map")
            return None

    def get_ratio(self, img):
        h, w = img.shape[:2]
        common = math.gcd(w, h)

        ratio_w = w // common
        ratio_h = h // common

        print(f'Input Image ratio: {ratio_w}:{ratio_h}')

        return (ratio_w, ratio_h), f"{ratio_w}r{ratio_h}"

    def get_factor(self, img1, img_shape):
        h1, w1 = img1.shape[:2]
        h2, w2 = img_shape

        factor_w = w1 / w2
        factor_h = h1 / h2

        return factor_w, factor_h

    def get_resized_img(self, img, size):
        """
        img: The source image object
        size: A tuple (width, height) e.g., (500, 800)
        """
        resized_img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
        return resized_img

    def get_resolution(self, img1):
        h1, w1 = img1.shape[:2]
        return h1, w1

    def match(self, main_img, template, threshold = 0.8):
        main_gray = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)
        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        w, h = template_gray.shape[::-1]

        # 3. Perform matching (TM_CCOEFF_NORMED is standard)
        result = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        # threshold = 0.8
        if max_val >= threshold:
            print(f"Match found at: {max_loc} with confidence {max_val:.2f}")

            # Draw a rectangle around the match
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(main_img, top_left, bottom_right, (0, 255, 0), 2)

            cv2.imshow('Result', main_img)
            # cv2.imwrite("result.png", main_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("No match found above the threshold.")

    def template_match(self, source_img):
        template_path = "template/"
        image = cv2.imread(source_img)
        img_ratio, ratio_code = self.get_ratio(image)
        template_image = None

        if os.path.exists(template_path + ratio_code + ".png"):
            template_image = cv2.imread(template_path + ratio_code + ".png")
        else:
            print(f"Template not found for ratio {ratio_code}")
            return None

        new_resolution = self.image_resolution_map(ratio_code)
        if new_resolution is None:
            print(f"Resolution not found for ratio {ratio_code}")
            return None

        new_image = self.get_resized_img(image, new_resolution)
        self.match(new_image, template_image, 0.8)

if __name__ == "__main__":
    tm = TemplateMatch()
    tm.template_match("images/800x500.png")