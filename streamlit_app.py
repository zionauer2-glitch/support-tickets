import streamlit as st
import json

st.set_page_config(page_title="Real Estate Prompt Generator", page_icon="🏡")

st.title("🏡 Real Estate Prompt Generator")
st.write("Generate professional AI real estate photo prompts and download as JSON.")

# Example 10 prompts
prompts = [
    "1. A sleek modern glass house with clean lines and minimalist landscaping, Canon EOS R5 + RF 15-35mm f/2.8L IS, photographed in soft morning light, IMG_9834.CR2, 8k_HDRi, editorial.archdigest, architectural digest cover.",
    "2. A rustic wooden cabin surrounded by autumn trees and mist, Nikon Z9 + NIKKOR Z 24-70mm f/2.8 S, captured at golden hour, ProRes_4444XQ, Leica. Summicron, cinematic drone aerial.",
    "3. A luxury beachfront villa with infinity pool overlooking turquoise water, Sony A7R IV + FE 12-24mm f/2.8 GM, photographed during blue hour, ACEScg, 8k_HDRi, luxury real estate brochure.",
    "4. A cozy Scandinavian interior living room with natural wood furniture and soft textiles, Fujifilm GFX100S + GF 45mm f/2.8 R WR, shot in bright daylight, ProRes_4444XQ, editorial.archdigest, interior staging.",
    "5. A dramatic hillside mansion with terraced gardens and night lighting, Canon 5D Mark IV + EF 24mm f/1.4L II, captured at twilight, IMG_9834.CR2, 8k_HDRi, cinematic drone aerial.",
    "6. A wide-angle showcase of a Mediterranean villa courtyard with fountains and stone arches, ARRI Alexa LF + Cooke Anamorphic/i 32mm, captured mid-day, ProRes_4444XQ, architectural digest cover.",
    "7. An elegant penthouse kitchen with marble countertops and panoramic city views, Leica SL2 + APO-Summicron-SL 28mm f/2 ASPH, shot in afternoon light, Leica. Summicron, HDRi, interior staging.",
    "8. A cinematic drone aerial of a futuristic smart home with solar panels, DJI Mavic 3 Cine Hasselblad L2D-20c, captured at sunset, ACEScg, ProRes_4444XQ, wide-angle showcase.",
    "9. A minimalist Japanese tatami room with sliding shoji doors, natural textures, Sony FX3 + FE 16-35mm f/2.8 GM, photographed in soft diffuse daylight, IMG_9834.CR2, editorial.archdigest, interior staging.",
    "10. A detailed close-up of a luxury bathroom vanity with golden fixtures and marble sink, Hasselblad H6D-100c + HC 80mm f/2.8, captured in warm evening light, 8k_HDRi, ProRes_4444XQ, luxury real estate brochure."
]

# Show prompts in app
st.subheader("Generated Prompts")
for p in prompts:
    st.write(p)

# Convert to JSON
data = {"real_estate_prompts": prompts}
json_data = json.dumps(data, indent=4)

# Download button
st.download_button(
    label="📥 Download JSON",
    data=json_data,
    file_name="real_estate_prompts.json",
    mime="application/json"
)