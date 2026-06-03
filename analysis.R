# Spatial regression diagnostics — NHIS Uninsurance Ghana
# Requires: spdep, spatialreg, dplyr, ggplot2
# Usage: Rscript analysis.R

library(spdep)
library(spatialreg)
library(dplyr)

cat("=== NHIS Uninsurance Spatial Diagnostics ===\n")
cat("Load district-level data and spatial weights before running.\n")

# Example workflow (uncomment with real data paths):
# df <- read.csv("data/processed/nhis_district_master.csv")
# coords <- cbind(df$longitude, df$latitude)
# knn <- knearneigh(coords, k = 4)
# nb  <- knn2nb(knn)
# lw  <- nb2listw(nb, style = "W")

# Global Moran's I
# moran_result <- moran.test(df$uninsurance_rate, lw)
# cat("Moran's I:", moran_result$estimate[1], "\n")
# cat("p-value:", moran_result$p.value, "\n")

# Spatial lag model
# slm <- lagsarlm(uninsurance_rate ~ poverty + illiteracy + healthcare_density,
#                 data = df, listw = lw)
# summary(slm)

cat("Done.\n")
