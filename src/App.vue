<template>
  <div id="app"></div>
</template>

<script>
import AMap from "AMap";
import AMapUI from "AMapUI";
export default {
  name: "App",
  data() {
    return {
      location: null,
      AMap: null,
      infoWindow: null,
    };
  },
  mounted() {
    this.map = new AMap.Map("app");
    this.map.on("complete", this.onComplete);
  },
  methods: {
    openInfoWindow: function (item) {
      const selected = item["address"] + "<br/>" + item["name"];
      if (this.infoWindow == null) {
        this.infoWindow = new AMap.InfoWindow({
          content: selected, //传入 dom 对象，或者 html 字符串
          autoMove: true,
          offset: [0, -30],
        });
      } else {
        this.infoWindow.setContent(selected);
      }

      // 打开信息窗体
      this.infoWindow.open(this.map, [item["lng"], item["lat"]]);
    },
    onComplete() {
      this.location = {
        AION: [
          {
            type: "AION",
            name: "广汽埃安上海星品宝黎环球港商超展示中心",
            address:
              "由上海市普陀区中山北路3300号上海环球港B1层变更至上海市普陀区中山北路3300号上海环球港4层",
            lng: 121.412622764546,
            lat: 31.233391222976,
          },
          {
            type: "AION",
            name: "广汽埃安上海君和体验中心",
            address: " 上海市普陀区金昌路1858号",
            lng: 121.343720499029,
            lat: 31.275719110262,
          },
          {
            type: "AION",
            name: "广汽埃安上海长岚展示中心",
            address: "上海市闵行区沪青平公路415-433号",
            lng: 121.344840446204,
            lat: 31.175799590546,
          },
          {
            type: "AION",
            name: "广汽埃安上海晋熙万泰商超展示中心",
            address: "上海市虹口区广灵二路259号（万泰广场）",
            lng: 121.47544097758,
            lat: 31.283784138339,
          },
          {
            type: "AION",
            name: "广汽埃安上海星品宝黎百联南方商超展示中心",
            address: "上海市闵行区沪闵路7250号百联南方购物中心2区1F-002号",
            lng: 121.400356039847,
            lat: 31.132110186757,
          },
          {
            type: "AION",
            name: "广汽埃安上海弘仁宝裕体验中心",
            address: " 上海市宝山区江杨南路1505号",
            lng: 121.467104743736,
            lat: 31.334667489683,
          },
          {
            type: "AION",
            name: "广汽埃安上海君和五角场万达商超展示中心",
            address: "上海市杨浦区淞沪路77号五角场万达广场",
            lng: 121.512791343282,
            lat: 31.301504892282,
          },
          {
            type: "AION",
            name: "广汽埃安上海星品宝黎体验中心",
            address: "上海市闵行区黎安路1399弄18号",
            lng: 121.352216780298,
            lat: 31.120698940372,
          },
          {
            type: "AION",
            name: "广汽埃安上海炜业龙阳体验中心",
            address: "上海市浦东新区龙阳路1277号",
            lng: 121.535034231591,
            lat: 31.198180470256,
          },
          {
            type: "AION",
            name: "广汽埃安上海劲立徐汇华泾天街商场展示中心",
            address: "上海市徐汇区华泾路459号L102龙湖上海华泾天街",
            lng: 121.451014155895,
            lat: 31.119339192969,
          },
          {
            type: "AION",
            name: "广汽埃安上海劲立体验中心",
            address: " 上海市青浦区嘉松中路799弄26号",
            lng: 121.213692909175,
            lat: 31.247542855212,
          },
          {
            type: "AION",
            name: "广汽埃安上海劲立颛桥万达商超展示中心",
            address: "上海市闵行区颛兴东路1570号（颛桥万达）",
            lng: 121.406329798023,
            lat: 31.071220751344,
          },
          {
            type: "AION",
            name: "广汽埃安上海成套体验中心",
            address: " 上海市闵行区三鲁公路889号",
            lng: 121.531388851726,
            lat: 31.034159844503,
          },
          {
            type: "AION",
            name: "广汽埃安上海晋熙上海车市体验中心",
            address: "上海市浦东新区沪南路4789弄311号",
            lng: 121.58918321289,
            lat: 31.069381010403,
          },
        ],
        Beijing: [
          {
            type: "Beijing",
            name: "上海吉绅汽车销售服务有限公司",
            address: "上海市嘉定区江桥镇金园一路235号",
            lng: 121.3189024168,
            lat: 31.260777847152,
          },
        ],
        R: [
          {
            type: "R",
            name: "R汽车 上海百联南方体验中心",
            address: "上海市闵行区沪闵路7250号百联南方购物中心2区1F-024",
            lng: 121.399908276874,
            lat: 31.131173389393,
          },
          {
            type: "R",
            name: "R汽车 上海新天地体验中心",
            address: "上海市黄浦区马当路347号",
            lng: 121.475439376419,
            lat: 31.214471961523,
          },
          {
            type: "R",
            name: "R汽车 上海南翔印象城体验中心",
            address: "上海市嘉定区南翔镇陈翔公路2299号L1-21",
            lng: 121.306765381682,
            lat: 31.30438266328,
          },
          {
            type: "R",
            name: "R汽车 上海陆家嘴尚悦湾体验中心",
            address: "上海市浦东新区银城路66号尚悦湾一层107a单元",
            lng: 121.50936212375,
            lat: 31.241099435789,
          },
          {
            type: "R",
            name: "R汽车 上海五角场万达广场体验中心",
            address: "上海市杨浦区淞沪路77号五角场万达L1301室",
            lng: 121.514750394512,
            lat: 31.30023839886,
          },
          {
            type: "R",
            name: "R汽车 上海张江长泰广场体验中心",
            address: "上海浦东金科路2889弄长泰广场6座D1-07A",
            lng: 121.601702079689,
            lat: 31.205069486654,
          },
          {
            type: "R",
            name: "R汽车 上海环球港体验中心",
            address: "上海市普陀区中山北路3300号环球港B1150",
            lng: 121.412883019567,
            lat: 31.233343308892,
          },
          {
            type: "R",
            name: "R汽车 上海九亭金地广场体验中心",
            address: "上海市松江区九亭镇沪亭北路99弄3号九亭金地广场L1-016",
            lng: 121.319589154963,
            lat: 31.139760063001,
          },
          {
            type: "R",
            name: "R汽车 上海虹口凯德龙之梦体验中心",
            address: "上海市虹口区西江湾路388号A幢01-4041",
            lng: 121.478280985882,
            lat: 31.270818774229,
          },
          {
            type: "R",
            name: "R汽车 上海浦东新达汇三林体验中心",
            address: "上海市浦东新区永泰路1058弄新达汇广场L1-111",
            lng: 121.526067656126,
            lat: 31.141733977684,
          },
          {
            type: "R",
            name: "R汽车 上海嘉定江桥万达体验中心",
            address: "上海市嘉定区金沙江西路1051弄万达广场1F1109--1110铺位",
            lng: 121.325322739654,
            lat: 31.240774854703,
          },
          {
            type: "R",
            name: "R汽车 上海普陀百联中环体验中心",
            address: "上海市普陀区真光路1288号 百联中环购物广场B区1楼",
            lng: 121.383256915355,
            lat: 31.246335597533,
          },
          {
            type: "R",
            name: "R汽车 上海松江万达广场体验中心",
            address: "上海市松江区广富林路658号万达广场1楼1029号铺位",
            lng: 121.243084843619,
            lat: 31.057753708902,
          },
          {
            type: "R",
            name: "R汽车 上海龙湖宝山天街体验中心",
            address: "上海市宝山区龙湖宝山天街丹霞山路50弄1号1F-60",
            lng: 121.361699660445,
            lat: 31.359005875977,
          },
          {
            type: "R",
            name: "R汽车 上海百联西郊体验中心",
            address: "上海市长宁区仙霞西路88号西郊百联购物广场1楼1122号店铺",
            lng: 121.370309526494,
            lat: 31.208832014837,
          },
          {
            type: "R",
            name: "R汽车 上海奉贤万达广场体验中心(待开业)",
            address:
              "上海市奉贤区南桥镇沪杭公路1608号（上海奉贤万达广场1010商铺）",
            lng: 121.447976659033,
            lat: 30.941776001763,
          },
          {
            type: "R",
            name: "R汽车 上海青浦吾悦广场体验中心",
            address: "上海市青浦区淀山湖大道218号吾悦广场一号门一楼038号",
            lng: 121.095353227894,
            lat: 31.144370044189,
          },
          {
            type: "R",
            name: "R汽车 龙湖上海闵行天街体验中心",
            address: " R汽车龙湖上海闵行天街体验中心",
            lng: 121.414961791587,
            lat: 31.025888926096,
          },
        ],
        JiHe: [
          {
            type: "JiHe",
            name: "上海晋熙汽车销售服务有限公司",
            address: "上海市浦东新区沪南公路4777弄258号",
            lng: 121.594253,
            lat: 31.077434,
          },
          {
            type: "JiHe",
            name: "上海弘仁星品汽车销售服务有限公司",
            address: "上海市杨浦区军工路1601号",
            lng: 121.532118,
            lat: 31.27991,
          },
          {
            type: "JiHe",
            name: "上海明友泓浩汽车销售有限公司",
            address: "上海市奉贤区南桥镇环城西路1488号",
            lng: 121.446832,
            lat: 30.933954,
          },
          {
            type: "JiHe",
            name: "上海天麦汽车销售服务有限公司",
            address: "上海市静安区沪太路1111号",
            lng: 121.432944,
            lat: 31.285993,
          },
          {
            type: "JiHe",
            name: "上海浦之利汽车有限公司",
            address: "上海市普陀区金沙江路2145号普罗娜广场B座一楼",
            lng: 121.374283,
            lat: 31.2424,
          },
          {
            type: "JiHe",
            name: "上海中隆汽车销售服务有限公司",
            address: "上海闵行区中春路7169号",
            lng: 121.351842,
            lat: 31.146194,
          },
          {
            type: "JiHe",
            name: "上海吉庆新能源汽车销售有限公司",
            address: "上海市松江区茸平路19号",
            lng: 121.261108,
            lat: 31.040244,
          },
        ],
        LingPao: [
          {
            type: "JiHe",
            name: "颛桥万达店",
            address: "上海市闵行区颛桥万达1楼1008铺零跑汽车",
            lng: 121.406334,
            lat: 31.071151,
          },
          {
            type: "JiHe",
            name: "马桥万达店",
            address: "上海市闵行区马桥万达一楼1057零跑体验中心",
            lng: 121.372951,
            lat: 31.023398,
          },
          {
            type: "JiHe",
            name: "九亭金地广场店",
            address: "上海市松江区沪亭北路99弄3号1楼L1026",
            lng: 121.318799,
            lat: 31.13923,
          },
          {
            type: "JiHe",
            name: "静安店",
            address: "上海市静安区万荣路1150号",
            lng: 121.440865,
            lat: 31.292187,
          },
          {
            type: "JiHe",
            name: "五角场店",
            address: "上海市杨浦区五角场万达B座1楼1137铺位零跑汽车",
            lng: 121.513303,
            lat: 31.301133,
          },
          {
            type: "JiHe",
            name: "嘉定宝龙城店",
            address: "上海市嘉定区阿克苏路1099号宝龙广场一楼142室",
            lng: 121.260559,
            lat: 31.345639,
          },
        ],
      };
      this.map.on("click", () => this.infoWindow.close());
      const colorMap = {
        Beijing: "purple",
        JiHe: "blue",
        AION: "yellow",
        R: "green",
        LingPao: "orange"
      };
      const nameMap = {
        Beijing: "北",
        JiHe: "几",
        AION: "埃",
        R: "R",
        LingPao: "零"
      }
      AMapUI.loadUI(["overlay/SimpleMarker"], (SimpleMarker) => {
        for (const brandName in this.location) {
          this.location[brandName].forEach((item) => {
            // console.log(item)

            const marker = new SimpleMarker({
              position: new AMap.LngLat(item["lng"], item["lat"]), // 经纬度对象，也可以是经纬度构成的一维数组[116.39, 39.9]
              iconLabel: nameMap[brandName],
              iconTheme: "fresh",
              iconStyle: colorMap[brandName],
            });
            marker.on("click", () => this.openInfoWindow(item));
            this.map.add(marker);
          });
        }
        this.map.setFitView();
      });
    },
  },
};
</script>

<style>
html,
body {
  margin: 0;
  padding: 0;
  height: 100%;
}
</style>

<style lang="less" scoped>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  width: 100%;
  height: 100%;
}
</style>
