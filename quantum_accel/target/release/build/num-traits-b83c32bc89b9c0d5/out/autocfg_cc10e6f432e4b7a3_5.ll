; ModuleID = 'autocfg_cc10e6f432e4b7a3_5.d9a92b23512306b9-cgu.0'
source_filename = "autocfg_cc10e6f432e4b7a3_5.d9a92b23512306b9-cgu.0"
target datalayout = "e-m:w-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-windows-msvc"

; core::f64::<impl f64>::copysign
; Function Attrs: inlinehint uwtable
define internal double @"_ZN4core3f6421_$LT$impl$u20$f64$GT$8copysign17he4b55e94f7a19a32E"(double %self, double %sign) unnamed_addr #0 {
start:
  %0 = alloca [8 x i8], align 8
  %1 = call double @llvm.copysign.f64(double %self, double %sign)
  store double %1, ptr %0, align 8
  %_0 = load double, ptr %0, align 8
  ret double %_0
}

; autocfg_cc10e6f432e4b7a3_5::probe
; Function Attrs: uwtable
define void @_ZN26autocfg_cc10e6f432e4b7a3_55probe17h53d8e5a2f3f80c46E() unnamed_addr #1 {
start:
; call core::f64::<impl f64>::copysign
  %_1 = call double @"_ZN4core3f6421_$LT$impl$u20$f64$GT$8copysign17he4b55e94f7a19a32E"(double 1.000000e+00, double -1.000000e+00)
  ret void
}

; Function Attrs: nocallback nofree nosync nounwind speculatable willreturn memory(none)
declare double @llvm.copysign.f64(double, double) #2

attributes #0 = { inlinehint uwtable "target-cpu"="x86-64" "target-features"="+cx16,+sse3,+sahf" }
attributes #1 = { uwtable "target-cpu"="x86-64" "target-features"="+cx16,+sse3,+sahf" }
attributes #2 = { nocallback nofree nosync nounwind speculatable willreturn memory(none) }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 8, !"PIC Level", i32 2}
!1 = !{!"rustc version 1.87.0 (17067e9ac 2025-05-09)"}
