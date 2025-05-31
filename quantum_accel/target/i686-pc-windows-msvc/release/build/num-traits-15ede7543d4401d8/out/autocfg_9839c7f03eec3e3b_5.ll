; ModuleID = 'autocfg_9839c7f03eec3e3b_5.568445bcaee9e23a-cgu.0'
source_filename = "autocfg_9839c7f03eec3e3b_5.568445bcaee9e23a-cgu.0"
target datalayout = "e-m:x-p:32:32-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32-a:0:32-S32"
target triple = "i686-pc-windows-msvc"

; core::f64::<impl f64>::copysign
; Function Attrs: inlinehint uwtable
define internal <8 x i8> @"_ZN4core3f6421_$LT$impl$u20$f64$GT$8copysign17h405dd4c1e3cd7ea1E"(double %self, double %sign) unnamed_addr #0 {
start:
  %_0 = alloca [8 x i8], align 8
  %0 = call double @llvm.copysign.f64(double %self, double %sign)
  store double %0, ptr %_0, align 8
  %1 = load <8 x i8>, ptr %_0, align 8
  ret <8 x i8> %1
}

; autocfg_9839c7f03eec3e3b_5::probe
; Function Attrs: uwtable
define void @_ZN26autocfg_9839c7f03eec3e3b_55probe17h2dcb5009d5c34e32E() unnamed_addr #1 {
start:
  %0 = alloca [8 x i8], align 8
  %1 = alloca [8 x i8], align 8
; call core::f64::<impl f64>::copysign
  %2 = call <8 x i8> @"_ZN4core3f6421_$LT$impl$u20$f64$GT$8copysign17h405dd4c1e3cd7ea1E"(double 1.000000e+00, double -1.000000e+00)
  store <8 x i8> %2, ptr %0, align 8
  call void @llvm.memcpy.p0.p0.i32(ptr align 8 %1, ptr align 8 %0, i32 8, i1 false)
  %_1 = load double, ptr %1, align 8
  ret void
}

; Function Attrs: nocallback nofree nosync nounwind speculatable willreturn memory(none)
declare double @llvm.copysign.f64(double, double) #2

; Function Attrs: nocallback nofree nounwind willreturn memory(argmem: readwrite)
declare void @llvm.memcpy.p0.p0.i32(ptr noalias nocapture writeonly, ptr noalias nocapture readonly, i32, i1 immarg) #3

attributes #0 = { inlinehint uwtable "target-cpu"="pentium4" }
attributes #1 = { uwtable "target-cpu"="pentium4" }
attributes #2 = { nocallback nofree nosync nounwind speculatable willreturn memory(none) }
attributes #3 = { nocallback nofree nounwind willreturn memory(argmem: readwrite) }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 8, !"PIC Level", i32 2}
!1 = !{!"rustc version 1.87.0 (17067e9ac 2025-05-09)"}
