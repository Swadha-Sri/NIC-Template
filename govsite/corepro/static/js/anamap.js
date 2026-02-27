(function () {
  function parseJsonScript(id, fallback) {
    const node = document.getElementById(id);
    if (!node) return fallback;
    try {
      return JSON.parse(node.textContent);
    } catch (error) {
      return fallback;
    }
  }

  function normalizeDistrictCode(rawCode) {
    if (rawCode === null || rawCode === undefined) {
      return "";
    }

    const asNumber = Number(rawCode);
    if (Number.isNaN(asNumber)) {
      return String(rawCode).trim();
    }

    return String(parseInt(asNumber, 10));
  }

  const MAP_SCALE = [
    "#f7fbff",
    "#deebf7",
    "#c6dbef",
    "#9ecae1",
    "#6baed6",
    "#3182bd",
    "#08519c",
    "#08458f",
    "#08306b",
    "#041b4d",
  ];

  function getColorFromScale(rate, scale) {
    const safeRate = Number.isFinite(rate) ? rate : 0;
    const clamped = Math.max(0, Math.min(100, safeRate));
    const index = Math.round((clamped / 100) * (scale.length - 1));
    return scale[index];
  }

  function getMapShade(rate) {
    return getColorFromScale(rate, MAP_SCALE);
  }

  function ensureMapLegend(mapId) {
    const mapContainer = document.getElementById(mapId);
    if (!mapContainer || !mapContainer.parentElement) {
      return;
    }

    const legendId = mapId + "Legend";
    const existingLegend = document.getElementById(legendId);
    if (existingLegend) {
      return;
    }

    const legend = document.createElement("div");
    legend.id = legendId;
    legend.className = "mt-2 d-flex align-items-center gap-2 flex-wrap";

    const title = document.createElement("span");
    title.className = "small fw-semibold";
    title.textContent = "Legend (Achievement %):";
    legend.appendChild(title);

    const ranges = [
      { label: "0–25", value: 12.5 },
      { label: "26–50", value: 37.5 },
      { label: "51–75", value: 62.5 },
      { label: "76–100", value: 87.5 },
    ];

    ranges.forEach(function (range) {
      const item = document.createElement("span");
      item.className = "d-inline-flex align-items-center gap-1 small";

      const swatch = document.createElement("span");
      swatch.style.display = "inline-block";
      swatch.style.width = "14px";
      swatch.style.height = "14px";
      swatch.style.border = "1px solid #000000";
      swatch.style.backgroundColor = getMapShade(range.value);

      const text = document.createElement("span");
      text.textContent = range.label;

      item.appendChild(swatch);
      item.appendChild(text);
      legend.appendChild(item);
    });

    mapContainer.parentElement.appendChild(legend);
  }

  function createNormalMap(mapId) {
    return L.map(mapId, {
      zoomControl: true,
      attributionControl: true,
      dragging: true,
      scrollWheelZoom: true,
      doubleClickZoom: true,
      boxZoom: true,
      keyboard: true,
      touchZoom: true,
    });
  }

  function addBaseLayer(mapObj) {
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: "&copy; OpenStreetMap contributors",
    }).addTo(mapObj);
  }

  function renderDistrictLayer(
    mapObj,
    geoJsonData,
    districtMetrics,
    colorResolver,
  ) {
    const layer = L.geoJSON(geoJsonData, {
      style: function (feature) {
        const districtCode = normalizeDistrictCode(feature.properties.dtcode11);
        const metrics = districtMetrics[districtCode] || {
          target: 0,
          installed: 0,
          achievement_rate: 0,
        };

        return {
          fillColor: colorResolver(metrics.achievement_rate || 0),
          weight: 1,
          opacity: 1,
          color: "#000000",
          fillOpacity: 0.8,
        };
      },
      onEachFeature: function (feature, layerRef) {
        const districtCode = normalizeDistrictCode(feature.properties.dtcode11);
        const districtName = feature.properties.dtname || "District";
        const metrics = districtMetrics[districtCode] || {
          target: 0,
          installed: 0,
          achievement_rate: 0,
        };

        layerRef.bindTooltip(
          "<strong>" +
            districtName +
            "</strong>" +
            "<br/>Target: " +
            Number(metrics.target || 0).toLocaleString() +
            "<br/>Installed: " +
            Number(metrics.installed || 0).toLocaleString() +
            "<br/>Achievement: " +
            Number(metrics.achievement_rate || 0).toFixed(2) +
            "%",
          { sticky: true },
        );
      },
    }).addTo(mapObj);

    mapObj.fitBounds(layer.getBounds(), { padding: [5, 5] });
  }

  document.addEventListener("DOMContentLoaded", function () {
    const mapYears = parseJsonScript("map-years", []);
    const averageMapData = parseJsonScript("average-map-data", {});
    const yearMapData = parseJsonScript("year-map-data", {});
    const rootNode = document.getElementById("anamapRoot");

    if (!rootNode) {
      return;
    }

    const geoJsonUrl = rootNode.dataset.geojsonUrl;
    const yearButtonsContainer = document.getElementById("yearButtons");
    const singleMapSection = document.getElementById("singleMapSection");
    const splitMapSection = document.getElementById("splitMapSection");
    const yearMapTitle = document.getElementById("yearMapTitle");

    let selectedYear = null;
    let singleAverageMap = null;
    let splitAverageMap = null;
    let selectedYearMap = null;
    let geoJsonData = null;

    function destroyMap(mapObj) {
      if (mapObj) {
        mapObj.remove();
      }
    }

    function buildYearButtons() {
      if (!yearButtonsContainer) {
        return;
      }

      yearButtonsContainer.innerHTML = "";

      mapYears.forEach(function (yearLabel) {
        const button = document.createElement("button");
        button.type = "button";
        button.className = "btn btn-outline-primary year-btn";
        button.textContent = yearLabel;
        button.dataset.year = yearLabel;

        button.addEventListener("click", function () {
          if (selectedYear === yearLabel) {
            selectedYear = null;
            showSingleView();
            return;
          }

          selectedYear = yearLabel;
          showSplitView(yearLabel);
        });

        yearButtonsContainer.appendChild(button);
      });
    }

    function updateButtonState() {
      const buttons = document.querySelectorAll(".year-btn");
      buttons.forEach(function (btn) {
        if (btn.dataset.year === selectedYear) {
          btn.classList.remove("btn-outline-primary");
          btn.classList.add("btn-primary");
        } else {
          btn.classList.remove("btn-primary");
          btn.classList.add("btn-outline-primary");
        }
      });
    }

    function showSingleView() {
      splitMapSection.classList.add("d-none");
      singleMapSection.classList.remove("d-none");

      destroyMap(splitAverageMap);
      destroyMap(selectedYearMap);
      splitAverageMap = null;
      selectedYearMap = null;

      destroyMap(singleAverageMap);
      singleAverageMap = createNormalMap("avgMapSingle");
      addBaseLayer(singleAverageMap);
      renderDistrictLayer(
        singleAverageMap,
        geoJsonData,
        averageMapData,
        getMapShade,
      );
      ensureMapLegend("avgMapSingle");

      updateButtonState();
    }

    function showSplitView(yearLabel) {
      singleMapSection.classList.add("d-none");
      splitMapSection.classList.remove("d-none");

      destroyMap(singleAverageMap);
      singleAverageMap = null;

      destroyMap(splitAverageMap);
      destroyMap(selectedYearMap);

      splitAverageMap = createNormalMap("avgMapSplit");
      selectedYearMap = createNormalMap("yearMap");

      addBaseLayer(splitAverageMap);
      addBaseLayer(selectedYearMap);

      const selectedYearData = yearMapData[yearLabel] || {};

      renderDistrictLayer(
        splitAverageMap,
        geoJsonData,
        averageMapData,
        getMapShade,
      );
      renderDistrictLayer(
        selectedYearMap,
        geoJsonData,
        selectedYearData,
        getMapShade,
      );
      ensureMapLegend("avgMapSplit");
      ensureMapLegend("yearMap");

      if (yearMapTitle) {
        yearMapTitle.textContent = yearLabel + " Achievement";
      }

      setTimeout(function () {
        splitAverageMap.invalidateSize();
        selectedYearMap.invalidateSize();
      }, 60);

      updateButtonState();
    }

    fetch(geoJsonUrl)
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        geoJsonData = data;
        buildYearButtons();
        showSingleView();
      })
      .catch(function () {
        if (yearButtonsContainer) {
          yearButtonsContainer.innerHTML =
            "<span class='text-danger'>Unable to load map data.</span>";
        }
      });
  });
})();
