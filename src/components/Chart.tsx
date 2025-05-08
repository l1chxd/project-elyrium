'use client';

import dynamic from 'next/dynamic';
import { useEffect, useState } from 'react';

const ApexChart = dynamic(() => import('react-apexcharts'), { ssr: false });

export default function Chart() {
  const [series, setSeries] = useState<any[]>([]);

  useEffect(() => {
    async function fetchData() {
      const res = await fetch(
        'https://api.coincap.io/v2/assets/bitcoin/history?interval=h1'
      );
      const data = await res.json();

      const prices = data.data.map((point: any) => ({
        time: new Date(point.time).toLocaleTimeString([], {
          hour: '2-digit',
          minute: '2-digit',
        }),
        price: parseFloat(point.priceUsd),
      }));

      console.log("📊 CoinCap Preise:", prices);

      setSeries([
        {
          name: 'BTC/USD',
          data: prices.map((p) => ({
            x: p.time,
            y: p.price,
          })),
        },
      ]);
    }

    fetchData();
  }, []);

  const options = {
    chart: {
      id: 'btc-chart',
      toolbar: { show: false },
    },
    xaxis: {
      type: 'category',
    },
    yaxis: {
      labels: {
        formatter: (value: number) => `$${value.toFixed(0)}`,
      },
    },
  };

  return (
    <div className="bg-white p-4 rounded shadow mt-8">
      <h2 className="text-xl font-semibold mb-2">📉 BTC/USD Verlauf (Demo)</h2>
      <ApexChart options={options} series={series} type="line" height={300} />
    </div>
  );
}