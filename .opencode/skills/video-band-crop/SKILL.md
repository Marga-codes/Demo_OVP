---
name: video-band-crop
description: Remove a white or light-gray horizontal band from the top/bottom edge of a video by measuring it across the timeline and cropping the frame. Use when a hero background video shows a white strip or light band at its edge ("franja blanca", "banda gris", "tiene una parte blanca", "quitar la franja superior del video", "recortar/redimensionar el video eliminando esa banda"). Works for mp4/mov/webm backgrounds and also crops an optional poster image.
---

# Cropping an edge band off a video

When a hero/background video shows a white or gray band at its top or bottom
edge, do NOT guess the crop by eye. Measure the band across the whole timeline,
crop with a safety margin, then verify in a browser.

## 1. Detect the band size

Run the helper (it samples frames every 0.5 s and returns pixel extents):

```bash
python3 .opencode/skills/video-band-crop/scripts/band-detect.py assets/<video>.mp4
# or: ... --every 1 --margin 20 --json
```

Read the printed `top`/`bottom` extents and the suggested `-vf "crop=W:H:X:Y"` string.

## 2. Crop the video

Re-encode with x264, keep the audio stream, and add faststart:

```bash
ffmpeg -y -v error -i assets/<video>.mp4 \
  -vf "crop=W:H:X:Y" \
  -c:v libx264 -crf 19 -preset medium -pix_fmt yuv420p -movflags +faststart \
  -c:a copy /tmp/cropped.mp4 \
  && mv /tmp/cropped.mp4 assets/<video>.mp4
```

Notes:
- `crop` only removes pixels (no stretching/distortion). Aspect changes are fine
  for objects displayed with `object-fit: cover`.
- Keep a margin of ~10–20 px past the last detected band row so a fractional
  band or video-compression edge never reappears, but do not cut real content.
- The band can be pure white (>230) or light gray (>170); the current thresholds
  catch both.

## 3. Crop the poster (if one exists)

If the page also uses `<video poster="assets/<poster>.jpg">`, crop the same
proportion so the pre-play frame matches:

```bash
ffmpeg -y -v error -i assets/<poster>.jpg -vf "crop=Wtop:Hscale:0:Xtop" /tmp/p.jpg \
  && mv /tmp/p.jpg assets/<poster>.jpg
```

## 4. Verify — never "by eye"

Confirm the band is really gone:

1. Re-run the detector on the output file and confirm `top`/`bottom` = margin only.
2. Browser check with agent-browser (real render, not assumed):
   ```bash
   agent-browser open http://localhost:<port>/<page>.html
   agent-browser eval "
     (()=>{const v=document.querySelector('.hero video');
      const c=document.createElement('canvas');c.width=v.videoWidth;c.height=v.videoHeight;
      const x=c.getContext('2d');x.drawImage(v,0,0);
      const d=x.getImageData(0,0,c.width,c.height).data,w=c.width,h=c.height;
      let max=0;
      for(let y=0;y<40;y++){let s=0,n=0;
        for(let i=y*w*4;i<(y+1)*w*4;i+=16){const l=(d[i]+d[i+1]+d[i+2])/3;s+=l;n++;}
        max=Math.max(max,s/n);}
      return 'max top-40 avg lum='+Math.round(max);})()"
   ```
   A value under ~160 means the top rows are dark (no white band). If it is still
   bright, re-run detection with a lower `--bright-min` and a larger `--margin`.