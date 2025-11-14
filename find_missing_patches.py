# from pathlib import Path

# prep = Path("/mnt/32TB/prh/proj/healnet/data/tcga/wsi/brca_preprocessed_level2")
# patches = {p.stem for p in prep.joinpath("patches").glob("*.h5")}
# features = {p.stem for p in prep.joinpath("patch_features").glob("*.pt")}
# missing = sorted(patches - features)
# print(f"缺失特征文件数：{len(missing)}")
# for name in missing:
#     print(name)

# one missing patch: TCGA-AR-A2LL-01Z-00-DX1.F0AF890C-2B34-4758-A929-58AAFF593EC5.pt


# 输出wsi图像的level
# import openslide
# slide = openslide.OpenSlide("/mnt/32TB/prh/proj/healnet/data/tcga/wsi/brca/TCGA-3C-AALJ-01Z-00-DX1.777C0957-255A-42F0-9EEB-A3606BCF0C96.svs")
# print(slide.level_dimensions)


from pathlib import Path
import h5py

base = Path("/mnt/32TB/prh/proj/healnet/data/tcga/wsi/brca_preprocessed_level2/patches")
bad = []
for h5_path in base.glob("*.h5"):
    try:
        with h5py.File(h5_path, "r") as f:
            _ = f["coords"][:]
    except Exception as exc:
        bad.append((h5_path.name, type(exc).__name__, str(exc)))
print(f"问题文件数：{len(bad)}")
for name, err, msg in bad:
    print(name, err, msg)
