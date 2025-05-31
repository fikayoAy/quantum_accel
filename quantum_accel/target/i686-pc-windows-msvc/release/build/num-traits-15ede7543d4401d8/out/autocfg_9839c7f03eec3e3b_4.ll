; ModuleID = 'autocfg_9839c7f03eec3e3b_4.3f435c0c5254798a-cgu.0'
source_filename = "autocfg_9839c7f03eec3e3b_4.3f435c0c5254798a-cgu.0"
target datalayout = "e-m:x-p:32:32-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32-a:0:32-S32"
target triple = "i686-pc-windows-msvc"

@alloc_e6758488a51c40069ade2309416f0500 = private unnamed_addr constant [6 x i8] c"<anon>", align 1
@alloc_5760cc517ece796840acf2ae2b53a0b1 = private unnamed_addr constant <{ ptr, [12 x i8] }> <{ ptr @alloc_e6758488a51c40069ade2309416f0500, [12 x i8] c"\06\00\00\00\01\00\00\00\1F\00\00\00" }>, align 4

; autocfg_9839c7f03eec3e3b_4::probe
; Function Attrs: uwtable
define void @_ZN26autocfg_9839c7f03eec3e3b_45probe17h76f40fb92811b99bE() unnamed_addr #0 {
start:
  ret void
}

; core::panicking::panic_const::panic_const_div_by_zero
; Function Attrs: cold noinline noreturn uwtable
declare void @_ZN4core9panicking11panic_const23panic_const_div_by_zero17h58d3ab757e6d5463E(ptr align 4) unnamed_addr #1

attributes #0 = { uwtable "target-cpu"="pentium4" }
attributes #1 = { cold noinline noreturn uwtable "target-cpu"="pentium4" }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 8, !"PIC Level", i32 2}
!1 = !{!"rustc version 1.87.0 (17067e9ac 2025-05-09)"}
