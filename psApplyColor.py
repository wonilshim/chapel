import bpy

# 머그컵 객체를 선택합니다.
mug = bpy.data.objects['Ball']

# 새로운 재질을 생성합니다.
new_material = bpy.data.materials.new(name="NewMaterial")
new_material.diffuse_color = (1, 0, 0, 1)  # 빨간색 (R, G, B, A)

# 머그컵에 새로운 재질을 할당합니다.
if mug.data.materials:
    mug.data.materials[0] = new_material
else:
    mug.data.materials.append(new_material)
