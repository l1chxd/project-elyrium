'use client';

import { useEffect, useState } from 'react';
import ReactApexChart from 'react-apexcharts';

export default function Chart() {
  const [series, setSeries] = useState<any[]>([]);
  const [categories, setCategories] = useState<string[]>([]);

  useEffect(() => {
    fetch('http://localhost:8001/btc-prices')
      .then((res) => res.json())
      .then((data) => {
        const prices = data.map((entry: any) => ({
          time: entry.time,
          price: parseFloat(entry.price),
        }));
        setCategories(prices.map((p) => p.time));
        setSeries([{ name: 'BTC/USD', data: prices.map((p) => p.price) }]);
      })
      .catch((err) => console.error('Fehler beim Laden der BTC-Preise:', err));
  }, []);

  return (
    <div className="bg-white shadow p-4 rounded mt-6">
      <h2 className="text-xl font-semibold mb-2">📈 BTC/USD Preisverlauf</h2>
      <ReactApexChart
        options={{
          chart: { type: 'line', zoom: { enabled: false } },
          xaxis: { categories },
          yaxis: {
            labels: { formatter: (val) => `$${val.toFixed(2)}` },
            min: undefined,
            max: undefined,
            forceNiceScale: true
          },
          stroke: { curve: 'smooth' },
        }}
        series={series}
        type="line"
        height={300}
      />
    </div>
  );
}
